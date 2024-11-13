#!/usr/bin/env python
import math
from dataclasses import dataclass
from codes import *


# Constants for sizes of group elements, field elements, and hashes in bits
BLS_FE_SIZE = 48.0 * 8.0
BLS_GE_SIZE = 48.0 * 8.0
PEDERSEN_FE_SIZE = 32.0 * 8.0
PEDERSEN_GE_SIZE = 33.0 * 8.0
HASH_SIZE = 256  # Assuming SHA256

@dataclass
class Scheme:
    code: Code  # code that is used
    com_size: int  # size of commitment in bits
    opening_overhead: int  # overhead of opening a symbol in the encoding

    def samples(self):
        '''
        The number of random samples needed to collect enough symbols except with small probability.
        '''
        return self.code.samples

    def total_comm(self):
        '''
        Compute the total communication in bits.
        '''
       # print('comm_per_query=',self.comm_per_query(),'self.samples=',self.samples())
        return self.comm_per_query() * self.samples()

    def comm_per_query(self):
        '''
        Compute the communication per query in bits.
        For LT code, codeword_len != Information bits about the location where the code to be passed is located. But there are ways to make it constant. We use log2 (k) for now.
        '''
        return math.log2(self.code.codeword_len) + self.opening_overhead + self.code.size_code_symbol
# self.code.codeword_len：表示编码的码字长度（码字中符号的数量）。
# math.log2(self.code.codeword_len)：计算码字长度的二进制对数，表示为了唯一标识一个符号所需的比特数。
# self.opening_overhead：在打开查询时附加的通信开销，以比特为单位。
# self.code.size_code_symbol：表示编码中每个符号的大小，以比特为单位。
    def encoding_size(self):
        '''
        Compute the size of the encoding in bits.
        '''
       # print(self.code.codeword_len, self.opening_overhead, self.code.size_code_symbol,self.code.codeword_len * (self.opening_overhead + self.code.size_code_symbol)/8000000000)
        return self.code.codeword_len * (self.opening_overhead + self.code.size_code_symbol)

    def reception(self):
        '''
        Compute the reception of the code.
        '''
        return self.code.reception

    def encoding_length(self):
        '''
        Compute the length of the encoding.
        '''
        return self.code.codeword_len

# Tensor Code Commitment
def makeTensorScheme(datasize, invrate=1):
    m = math.ceil(datasize / BLS_FE_SIZE)
    k = math.ceil(math.sqrt(m))
    # (datasize,k)
    n = invrate * k
    rs = makeRSCode(BLS_FE_SIZE, k, n)
    return Scheme(
        code=rs.tensor(rs),
        com_size=BLS_GE_SIZE * k,
        opening_overhead=BLS_GE_SIZE
    )

# Hash-Based Code Commitment
def makeHashBasedScheme(datasize, fsize=32, P=8, L=64, invrate=2):
    
    m = math.ceil(datasize / fsize)
    k = math.ceil(math.sqrt(m))
    n = invrate * k
    print(k,n)
    rs = makeRSCode(fsize, k, n)
  
    return Scheme(
        code=rs.interleave(k),
        com_size=n * HASH_SIZE + P * n * fsize + L * k * fsize,
        opening_overhead=0
    )

# Homomorphic Hash-Based Code Commitment with Pedersen Hash
def makeHomHashBasedScheme(datasize, P=2, L=2, invrate=4):
    m = math.ceil(datasize / PEDERSEN_FE_SIZE)
    k = math.ceil(math.sqrt(m))
    n = invrate * k
    rs = makeRSCode(PEDERSEN_FE_SIZE, k, n)
    return Scheme(
        code=rs.interleave(k),
        com_size=n * PEDERSEN_GE_SIZE + P * n * PEDERSEN_FE_SIZE + L * k * PEDERSEN_FE_SIZE,
        opening_overhead=0
    )

# Naive scheme
def makeNaiveScheme(datasize):
    return Scheme(
        code=Code(
            size_msg_symbol=datasize,
            msg_len=1,
            size_code_symbol=datasize,
            codeword_len=1,
            reception=1,
            samples=1
        ),
        com_size=HASH_SIZE,
        opening_overhead=0
    )

# Merkle scheme
def makeMerkleScheme(datasize, chunksize=1024):
    k = math.ceil(datasize / chunksize)
    return Scheme(
        code=makeTrivialCode(chunksize, k),
        com_size=HASH_SIZE,
        opening_overhead=math.ceil(math.log2(k)) * HASH_SIZE
    )

# KZG Commitment
def makeKZGScheme(datasize, invrate=1):
    k = math.ceil(datasize / BLS_FE_SIZE)
    print(datasize,k)
    # print(datasize,k)
    return Scheme(
        code=makeRSCode(BLS_FE_SIZE, k, invrate * k),
        com_size=BLS_GE_SIZE,
        opening_overhead=BLS_GE_SIZE
    )

# LT code with KZG Commitment scheme
def makeLTKZGScheme(datasize, invrate=1):
    k = math.ceil(datasize / BLS_FE_SIZE)
    # print(datasize,k)
    return Scheme(
        code=makeLTCode(BLS_FE_SIZE, k, invrate * k),
        com_size=BLS_GE_SIZE * k,
        opening_overhead=BLS_GE_SIZE
    )

# Tensor Code Commitment with row RS and column identity code scheme
def makeTensorRSIdentityScheme(datasize, invrate=1):
    m = math.ceil(datasize / BLS_FE_SIZE)
    k = math.ceil(math.sqrt(m))
    
    # print(datasize,k)
    n = invrate * k
    tc = makeTrivialCode(BLS_FE_SIZE, k)
    rs = makeRSCode(BLS_FE_SIZE, k, n)

    return Scheme(
        code=rs.tensor(tc),
        # Commit on row wise
        com_size=BLS_GE_SIZE * k,
        opening_overhead=BLS_GE_SIZE
    )

# Tensor Code Commitment with row LT sampling and column identity code
def makeTensorLTIdentityScheme(datasize, invrate=1):
    m = math.ceil(datasize / BLS_FE_SIZE)
    k = math.ceil(math.sqrt(m))

    # print(datasize,k)
    n = invrate * k
    tc = makeTrivialCode(BLS_FE_SIZE, k)
    rs = makeRSCode(BLS_FE_SIZE, k, n)
    
    return Scheme(
        code=rs.ltextend(tc),
        # Commit on column wise
        com_size=BLS_GE_SIZE * k,
        opening_overhead=BLS_GE_SIZE
    )
