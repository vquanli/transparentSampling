from dataclasses import dataclass
import math
import pandas as pd
# Statistical Security Parameter for Soundness
SECPAR_SOUND = 40

@dataclass
class Code:
    size_msg_symbol: int  # size of one symbol in the message
    size_code_symbol: int  # size of one symbol in the code
    msg_len: int  # number of symbols in the message
    codeword_len: int  # number of symbols in the codeword
    reception: int  # number of symbols needed to reconstruct (worst case)
    samples: int  # number of random samples to reconstruct with high probability

    def interleave(self, ell):
        return Code(
            size_msg_symbol=self.size_msg_symbol * ell,
            size_code_symbol=self.size_code_symbol * ell,
            msg_len=self.msg_len,
            codeword_len=self.codeword_len,
            reception=self.reception,
            samples=self.samples
        )

    def tensor(self, col):
        assert self.size_msg_symbol == col.size_msg_symbol
        assert self.size_code_symbol == col.size_code_symbol
        assert self.size_msg_symbol == self.size_code_symbol

        row_dist = self.codeword_len - self.reception + 1
        col_dist = col.codeword_len - col.reception + 1
        codeword_len = self.codeword_len * col.codeword_len

        '''
        Example:
        D D | o o
        D D | o o
        --- -+---
        o o | o o
        o o | o o
        Where D is the data.
        The reception is 8, since 7 is not enough to reconstruct:
        o o | o x
        o o | o x
        --- -+---
        o o | o x
        x x | x x
        Given the symbols marked with x, I cannot reconstruct the data.
        '''
        reception = codeword_len - row_dist * col_dist + 1

        # samples_via_reception = samples_from_reception(SECPAR_SOUND, reception, codeword_len)
        # loge = math.log2(math.e)
        # lognc = math.log2(col.codeword_len)
        # lognr = math.log2(self.codeword_len)
        # logbinomr = (self.reception - 1) * (lognr + loge - math.log2(self.reception - 1))
        # loginnerr = math.log2(1.0 - (self.codeword_len - self.reception + 1) / codeword_len)
        # logbinomc = (col.reception - 1) * (lognc + loge - math.log2(col.reception - 1))
        # loginnerc = math.log2(1.0 - (col.codeword_len - col.reception + 1) / codeword_len)

        # samples_direct_via_rows = int(math.ceil(-(lognc + logbinomr + SECPAR_SOUND) / loginnerr))
        # samples_direct_via_cols = int(math.ceil(-(lognr + logbinomc + SECPAR_SOUND) / loginnerc))
        # samples_direct = min(samples_direct_via_rows, samples_direct_via_cols)

        # samples = min(samples_direct, samples_via_reception)

        # Samples from Monte Carlo simulation
        # The essence is the same as the formula above, but the specific performance is obtained from the high-volume simulation.
        # Doubt the coupon bound formula is appropriate
        samples_via_reception = samples_from_reception(reception/codeword_len, codeword_len)
        samples = samples_via_reception
        
        return Code(
            size_msg_symbol=self.size_msg_symbol,
            msg_len=self.msg_len * col.msg_len,
            size_code_symbol=self.size_code_symbol,
            codeword_len=codeword_len,
            reception=reception,
            samples=samples
        )

    # Two dimension LT sampling for identify code and RS code
    def ltextend(self, col):
        assert self.size_msg_symbol == col.size_msg_symbol
        assert self.size_code_symbol == col.size_code_symbol
        assert self.size_msg_symbol == self.size_code_symbol

        row_dist = self.codeword_len - self.reception + 1
        col_dist = col.codeword_len - col.reception + 1
        codeword_len = self.codeword_len * col.codeword_len

        reception = codeword_len - row_dist * col_dist + 1
        

        n = max(self.codeword_len, col.codeword_len)
        k = min(self.codeword_len, col.codeword_len)

        # LT sample bound (still has some issues when compare with the coupon bound from the code, and doubt the coupon bound formula is appropriate.)
        # c is a constant and should be lager than 1. 
        # t=cnm.
        # c = 1.2
        # d=c
        # samples=n * (k+ c * math.sqrt(k) * math.log(k / (2**(-SECPAR_SOUND)))**2+ d * math.sqrt(k) * math.log(n / k))
        # print("k=",k,"c * math.sqrt(k) * math.log(k / (2**(-SECPAR_SOUND))) ** 2=",c * math.sqrt(k) * math.log2(k / (2**(-SECPAR_SOUND))),"d * math.sqrt(k) * math.log(n / k)=",d * math.sqrt(k) * math.log(n / k))

        # Samples from Monte Carlo simulation
        # The essence is the same as the formula above, but the specific performance is obtained from the high-volume simulation.
        samples = n * samples_from_reception_LT(k/n, n) + SECPAR_SOUND

        
        return Code(
            size_msg_symbol=self.size_msg_symbol,
            msg_len=self.msg_len * col.msg_len,
            size_code_symbol=self.size_code_symbol,
            codeword_len=codeword_len,
            reception=reception,
            samples=samples
        )

    def __eq__(self, other):
        return (
            self.size_msg_symbol == other.size_msg_symbol
            and self.size_code_symbol == other.size_code_symbol
            and self.msg_len == other.msg_len
            and self.codeword_len == other.codeword_len
            and self.reception == other.reception
        )

    def is_identity(self):
        return (
            self.size_msg_symbol == self.size_code_symbol
            and self.msg_len == self.codeword_len
        )



def samples_from_reception(k_n, n):
    k_n = float(f"{k_n:.2f}")
    df = pd.read_csv(f"./{k_n}/wr.csv", header=None)
    print('k_n=', k_n, 'n=', n)
    # 确保第一列数据类型为整数（根据需要）
    df[0] = df[0].astype(int)
    # 创建布尔掩码
    mask = df.iloc[:, 0] == n
    # 提取对应的样本值
    samples = df.loc[mask, 1].tolist()
    print('samples:', samples)
    # 返回样本值
    return samples[0] 


# def samples_from_reception_LT(k_n, reception):
#     df = pd.read_csv(f"./{k_n}/ltcode_bp.csv", header=None)
#     print('k_n=', k_n, 'reception=', reception)
#     mask = df.iloc[0, :] == reception
#     samples = df.loc[mask, 1].tolist()
#     print(samples)
#     return samples[0]
def samples_from_reception_LT(k_n, n):
    k_n = float(f"{k_n:.2f}")
    df = pd.read_csv(f"./{k_n}/ltcode_bp.csv", header=None)
    print('k_n=', k_n, 'n=', n)
    # 确保第一列数据类型为整数（根据需要）
    df[0] = df[0].astype(int)
    # 创建布尔掩码
    mask = df.iloc[:, 0] == n
    # n
    samples = df.loc[mask, 1].tolist()
    print('samples:', samples)
    # 返回样本值
    return samples[0] 


# def samples_from_reception_LT(k_n, reception):
#     df = pd.read_csv(f"./{k_n}/ltcode_bp.csv")
#     print('k_n=', k_n, 'reception=', reception)
#     first_value = df.iloc[0, 0]  # Get the value from the first row, first column
#     print(first_value)
#     return first_value

def harmonic_sum_modified(k):
    if k < 2:
        raise ValueError("k should be greater than or equal to 2 to avoid division by zero.")
    
    result = 0
    for i in range(2, int(k) + 1):
        result += 1 / (i - 1)
    
    return result
def calculate_R(k, sec_par):
    c=0.05

    """
    计算鲁棒孤立子分布中的参数 R。

    参数:
    k (int): 数据包数量，即输入符号数量。
    c (float): 调节常数，默认值为 0.05。
    sec_par (float): 2**(-sec_par)为解码失败概率允许值，默认值为 0.05。

    返回:
    float: 计算得到的 R 值。
    """
    return c * math.log(k / (2**(-sec_par))) * math.sqrt(k)

# Identity code
def makeTrivialCode(chunksize, k):
    return Code(
        size_msg_symbol=chunksize,
        msg_len=k,
        size_code_symbol=chunksize,
        codeword_len=k,
        reception=k,
        samples=samples_from_reception(k, k)
    )

# Reed-Solomon Code
# Polynomial of degree k - 1 over field with field element length fsize
# Evaluated at n points
def makeRSCode(fsize, k, n):
    assert k <= n
   # assert 2**fsize >= n, 'no such Reed-Solomon code :('
    return Code(
        size_msg_symbol=fsize,
        msg_len=k,
        size_code_symbol=fsize,
        codeword_len=n,
        reception=k,
        samples=samples_from_reception(k/n, n)
    )

# Ludy Transform Code
# Polynomial of degree k - 1 over field with field element length fsize
# Evaluated at n points
def makeLTCode(fsize, k, n):
    assert k <= n
    return Code(
        size_msg_symbol=fsize,
        msg_len=k,
        size_code_symbol=fsize,
        # LT code will encode on the fly, s.t. during the sampling, so only the original data need to be stored. Which bring more linear homomorphic operation of KZG. n==k.
        codeword_len=k,
        reception=k,
        samples=samples_from_reception_LT(k/n, n)
    )
#=204.94+1.24x+8.85×(10^−6)(x^2)
# tests
# assert makeRSCode (5 , 2, 4) . tensor ( makeRSCode (5 , 2 , 4) ). reception == 8
# assert makeRSCode (5 , 2, 4) . reception == 2