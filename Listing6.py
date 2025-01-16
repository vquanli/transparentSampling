#!/usr/bin/env python
import math
import sys
import csv
import os
from schemes import *
from fri import *
import numpy as np
DATASIZEUNIT = 8000000 # Megabytes
#本次修改的目的是固定k，计算n在一定范围内变化的，算法性能指标
# DATASIZEUNIT = 80000 # Megabytes
NSIZERANGE = range(2, 156,16)
NSIZERANGE = [1] + list(NSIZERANGE)
# DATASIZERANGE = np.arange(0.049152, 0.098304, 0.006144)
# k_n=[1,0.75,0.5]
non_s1=["fri"]
def writeCSV(path, d):
        # 如果目录不存在，则创建目录
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
    samples={}
    # for kn in k_n:
    datasize = 100* DATASIZEUNIT
    for s in NSIZERANGE:
        if s==1 and name in non_s1:
            continue
        scheme = makeScheme(datasize,invrate=s)
        commitment[s] = scheme.com_size / 8000000  # MB
        commpq[s] = scheme.comm_per_query() / 8000  # KB
        commtotal[s] = scheme.total_comm() / 8000000000  # GB
        encoding[s] = scheme.encoding_size() / 8000000000  # GB
    
    if not os.path.exists("./csvdata/"):
        os.makedirs("./csvdata/")

    # writeCSV(f"./csvdata/K_N={kn}/{name}_com.csv", commitment)
    # writeCSV(f"./csvdata/K_N={kn}/{name}_comm_pq.csv", commpq)
    # writeCSV(f"./csvdata/K_N={kn}/{name}_comm_total.csv", commtotal)
    # writeCSV(f"./csvdata/K_N={kn}/{name}_encoding.csv", encoding)
    writeCSV(f"./csvdata/{name}_com.csv", commitment)
    writeCSV(f"./csvdata/{name}_comm_pq.csv", commpq)
    writeCSV(f"./csvdata/{name}_comm_total.csv", commtotal)
    writeCSV(f"./csvdata/{name}_encoding.csv", encoding)

# ###########################################
writeScheme("rs", makeKZGScheme)
#writeScheme("merkle", makeMerkleScheme)
writeScheme("tensor", makeTensorScheme)
writeScheme("hash", makeHashBasedScheme)
writeScheme("homhash", makeHomHashBasedScheme)
writeScheme("fri", makeFRIScheme)
writeScheme("lt", makeLTKZGScheme)
writeScheme("tensorRSIdentity", makeTensorRSIdentityScheme)
writeScheme("tensorLTIdentity", makeTensorLTIdentityScheme)