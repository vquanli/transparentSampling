#!/usr/bin/env python
import math
from schemes import *

GRINDING = 20
RO_QUERIES = 60
STATISTICAL_SECURITY = 40
FRI_SOUNDNESS = STATISTICAL_SECURITY + RO_QUERIES - GRINDING

# k = number of field elements to represent the data --> number of rounds
def friNumRounds(mink, fanin, basedimension):
    # if we do no round, we can represent basedimension many elements
    # if we do one round, we can represent basedimension * fanin many elements
    # if we do r rounds, we can represent basedimension * (fanin ** r) many elements
    dimension = basedimension
    rnd = 0
    while dimension < mink:
        dimension *= fanin
        rnd += 1
    return rnd

# rate, size of first evaluation domain LLL_0, field size --> number of repetitions of query phase
def friNumRepetitions(rate, domainsize, fsize, batchsize, fanin):
    # ensure that the soundness error induced by LuckySet (e.g., distortion) is small
    maxbf = max(fanin, batchsize)
    logeps1 = 1 + math.ceil(math.log2(domainsize * (maxbf - 1))) - fsize
    assert logeps1 <= -FRI_SOUNDNESS, "Soundness error exceeds acceptable limits."

    # determine number of repetitions such that the soundness error related to the query phase is small
    deltastar = 0.5 * (1.0 - rate)
    base = 1.0 - deltastar
    logbase = math.log2(base)
    assert logbase < 0, "Invalid log base detected."
    L = -FRI_SOUNDNESS / logbase
    return math.ceil(L)

def makeFRIScheme(datasize, invrate=4, fsize=128, verbose=False):
    # determine k, should be "compatible" with the fan-in
    minfe = math.ceil(datasize / fsize)
    if verbose:
        print(f"Need at least dimension minfe = {minfe} field elements to represent the data.")

    # find good batchsize, fanin, and base dimension
    (batchsize, fanin, basedimension) = friGoodParameters(minfe, fsize, invrate)
    mink = math.ceil(minfe / batchsize)
    if verbose:
        print(f"With batch size B = {batchsize}, we need at least dimension mink = {mink}")
        print(f"Use fanin F = {fanin} and base dimension = {basedimension}")

    # determine number of rounds to get at least dimension mink in the base layer
    r = friNumRounds(mink, fanin, basedimension)
    if verbose:
        print(f"Need {r} rounds.")

    # calculate actual k and n
    k = basedimension * (fanin ** r)
    n = invrate * k
    rate = 1.0 / invrate
    if verbose:
        print(f"Need dimension k = {k} and evaluation domain size n = {n}.")

    # calculate number of repetitions for soundness guarantees
    L = friNumRepetitions(rate, n, fsize, batchsize, fanin)
    if verbose:
        print(f"Need {L} repetitions of the query phase.")

    # calculate size of one opening
    authsize = friAuthSize(n, rate, fsize, batchsize, fanin, basedimension)

    # compile the scheme
    rs = makeRSCode(fsize, k, n)

    # include all openings for the final layer in the commitment, no Merkle root for it
    final = basedimension * fsize
    openings = L * authsize
    roots = r * HASH_SIZE + (batchsize > 1) * HASH_SIZE

    return Scheme(
        com_size=roots + final + openings,
        code=rs.interleave(batchsize),
        opening_overhead=authsize - batchsize * fsize,
    )

# OPTIMIZATION SECTION
# given the minimum number of field elements we need to represent (minfe),
# the field size (fsize), the inverse rate (invrate), the basedimension, and
# the fanin, this function computes a good batchsize.
def friGoodBatchsize(minfe, fsize, invrate, basedimension, fanin):
    batchsizerange = range(1, 257)
    batchsize = 1
    mink = math.ceil(minfe / batchsize)
    r = friNumRounds(mink, fanin, basedimension)
    minauthsize = friAuthSize(basedimension * (fanin ** r) * invrate, 1.0 / invrate, fsize, batchsize, fanin, basedimension)
    for b in batchsizerange:
        mink = math.ceil(minfe / b)
        r = friNumRounds(mink, fanin, basedimension)
        currauthsize = friAuthSize(basedimension * (fanin ** r) * invrate, 1.0 / invrate, fsize, b, fanin, basedimension)
        if currauthsize <= minauthsize:
            batchsize = b
            minauthsize = currauthsize
    return batchsize

# computes (batchsize, fanin, basedimension) for FRI that works reasonably well.
def friGoodParameters(minfe, fsize, invrate):
    faninrange = [4, 8, 16]
    basedimensionrange = [2, 4, 6, 8, 16, 32, 64, 128]
    optfanin = 0
    optbasedimension = 0
    optbatchsize = 0
    mingap = -1
    for fanin in faninrange:
        for basedimension in basedimensionrange:
            batchsize = friGoodBatchsize(minfe, fsize, invrate, basedimension, fanin)
            mink = math.ceil(minfe / batchsize)
            r = friNumRounds(mink, fanin, basedimension)
            gap = basedimension * (fanin ** r) - mink
            if mingap == -1 or (gap >= 0 and gap <= mingap):
                mingap = gap
                optfanin = fanin
                optbasedimension = basedimension
                optbatchsize = batchsize
    return (optbatchsize, optfanin, optbasedimension)

# size of one opening (Merkle path + element)
def sizeMerkleOpening(numleafs, tuplesize, fsize):
    tupleItself = tuplesize * fsize
    sibling = tuplesize * fsize
    treedepth = math.ceil(math.log2(numleafs))
    copath = (treedepth - 1) * HASH_SIZE
    return tupleItself + sibling + copath

# size of the information needed to open one position in the FRI base layer
def friAuthSize(domainsize, rate, fsize, batchsize, fanin, basedimension):
    size = 0
    if batchsize > 1:
        size += sizeMerkleOpening(domainsize, batchsize, fsize)
    ncurr = domainsize
    while ncurr * rate > basedimension:
        numleafs = ncurr // fanin
        size += sizeMerkleOpening(numleafs, fanin, fsize)
        ncurr = numleafs
    return size
