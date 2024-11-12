#!/usr/bin/env python
import math
import sys
import csv
import os
from schemes import *
from fri import *

DATASIZEUNIT = 8000 * 1000  # Megabytes
DATASIZERANGE = range(1, 156, 15)

def writeCSV(path, d):
    with open(path, mode="w", newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        for x in d:
            writer.writerow([x, d[x]])

# Writes the graphs for a given scheme into a CSV file
def writeScheme(name, makeScheme):
    commitment = {}
    commpq = {}
    commtotal = {}
    encoding = {}

    for s in DATASIZERANGE:
        datasize = s * DATASIZEUNIT
        scheme = makeScheme(datasize)
        commitment[s] = scheme.com_size / 8000000  # MB
        commpq[s] = scheme.comm_per_query() / 8000  # KB
        commtotal[s] = scheme.total_comm() / 8000000000  # GB
        encoding[s] = scheme.encoding_size() / 8000000000  # GB

    if not os.path.exists("./csvdata/"):
        os.makedirs("./csvdata/")

    writeCSV(f"./csvdata/{name}_com.csv", commitment)
    writeCSV(f"./csvdata/{name}_comm_pq.csv", commpq)
    writeCSV(f"./csvdata/{name}_comm_total.csv", commtotal)
    writeCSV(f"./csvdata/{name}_encoding.csv", encoding)

# ###########################################
writeScheme("rs", makeKZGScheme)
writeScheme("tensor", makeTensorScheme)
writeScheme("hash", makeHashBasedScheme)
writeScheme("homhash", makeHomHashBasedScheme)
writeScheme("fri", makeFRIScheme)
writeScheme("lt", makeLT_KZGScheme)