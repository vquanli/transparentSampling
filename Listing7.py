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
DATASIZEUNIT = 80000 # Megabytes
NSIZERANGE = [2 ** (2 ** i) for i in range(11)]  # 生成 2^-1 到 2^-2048 的范围
K=[1024,2048,4096]
# DATASIZERANGE = np.arange(0.049152, 0.098304, 0.006144)
# k_n=[1,0.75,0.5]
non_s1=["fri"]
def writeCSV(path, d):
        # 如果目录不存在，则创建目录
    with open(path, mode="w", newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        for x in d:
            writer.writerow([x, d[x]])

def writeScheme(name, makeScheme):
    if not os.path.exists("./csvdata/"):
        os.makedirs("./csvdata/")
    
    for k in K:
        samples = {}
        datasize = k *DATASIZEUNIT
        for s in NSIZERANGE:
            scheme = makeScheme(datasize, invrate=s)
            log_s = math.log2(s)
            samples[log_s] = scheme.samples()  
        
        # 为每个 k 值生成一个单独的 CSV 文件
        writeCSV(f"./csvdata/{name}_samples_k={k}.csv", samples)
    # writeCSV(f"./csvdata/K_N={kn}/{name}_com.csv", commitment)
    # writeCSV(f"./csvdata/K_N={kn}/{name}_comm_pq.csv", commpq)
    # writeCSV(f"./csvdata/K_N={kn}/{name}_comm_total.csv", commtotal)
    # writeCSV(f"./csvdata/K_N={kn}/{name}_encoding.csv", encoding)
    # writeCSV(f"./csvdata/{name}_com.csv", commitment)
    # writeCSV(f"./csvdata/{name}_comm_pq.csv", commpq)
    # writeCSV(f"./csvdata/{name}_comm_total.csv", commtotal)
    # writeCSV(f"./csvdata/{name}_encoding.csv", encoding)
    #writeCSV(f"./csvdata/{name}_samples.csv", samples)

# ###########################################
# writeScheme("rs", makeKZGScheme)
# #writeScheme("merkle", makeMerkleScheme)
# writeScheme("tensor", makeTensorScheme)
writeScheme("hash", makeHashBasedScheme)
# writeScheme("homhash", makeHomHashBasedScheme)
# writeScheme("fri", makeFRIScheme)
# writeScheme("lt", makeLTKZGScheme)
# writeScheme("tensorRSIdentity", makeTensorRSIdentityScheme)
# writeScheme("tensorLTIdentity", makeTensorLTIdentityScheme)