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

        samples_via_reception = samples_from_reception(SECPAR_SOUND, reception, codeword_len)
        loge = math.log2(math.e)
        lognc = math.log2(col.codeword_len)
        lognr = math.log2(self.codeword_len)
        logbinomr = (self.reception - 1) * (lognr + loge - math.log2(self.reception - 1))
        loginnerr = math.log2(1.0 - (self.codeword_len - self.reception + 1) / codeword_len)
        logbinomc = (col.reception - 1) * (lognc + loge - math.log2(col.reception - 1))
        loginnerc = math.log2(1.0 - (col.codeword_len - col.reception + 1) / codeword_len)

        samples_direct_via_rows = int(math.ceil(-(lognc + logbinomr + SECPAR_SOUND) / loginnerr))
        samples_direct_via_cols = int(math.ceil(-(lognr + logbinomc + SECPAR_SOUND) / loginnerc))
        samples_direct = min(samples_direct_via_rows, samples_direct_via_cols)

        samples = min(samples_direct, samples_via_reception)
        return Code(
            size_msg_symbol=self.size_msg_symbol,
            msg_len=self.msg_len * col.msg_len,
            size_code_symbol=self.size_code_symbol,
            codeword_len=codeword_len,
            reception=reception,
            samples=samples
        )
    # def tensor(self, col):
    #     assert self.size_msg_symbol == col.size_msg_symbol
    #     assert self.size_code_symbol == col.size_code_symbol
    #     assert self.size_msg_symbol == self.size_code_symbol
    
    #     row_dist = self.codeword_len - self.reception + 1
    #     col_dist = col.codeword_len - col.reception + 1
    #     codeword_len = self.codeword_len * col.codeword_len

    #     '''
    #     Example:
    #     D D | o o
    #     D D | o o
    #     --- -+---
    #     o o | o o
    #     o o | o o
    #     Where D is the data.
    #     The reception is 8, since 7 is not enough to reconstruct:
    #     o o | o x
    #     o o | o x
    #     --- -+---
    #     o o | o x
    #     x x | x x
    #     Given the symbols marked with x, I cannot reconstruct the data.
    #     '''
    #     reception = codeword_len - row_dist * col_dist + 1

    #     # samples_via_reception = samples_from_reception(SECPAR_SOUND, reception, codeword_len)
    #     # loge = math.log2(math.e)
    #     # lognc = math.log2(col.codeword_len)
    #     # lognr = math.log2(self.codeword_len)
    #     # logbinomr = (self.reception - 1) * (lognr + loge - math.log2(self.reception - 1))
    #     # loginnerr = math.log2(1.0 - (self.codeword_len - self.reception + 1) / codeword_len)
    #     # logbinomc = (col.reception - 1) * (lognc + loge - math.log2(col.reception - 1))
    #     # loginnerc = math.log2(1.0 - (col.codeword_len - col.reception + 1) / codeword_len)

    #     # samples_direct_via_rows = int(math.ceil(-(lognc + logbinomr + SECPAR_SOUND) / loginnerr))
    #     # samples_direct_via_cols = int(math.ceil(-(lognr + logbinomc + SECPAR_SOUND) / loginnerc))
    #     # samples_direct = min(samples_direct_via_rows, samples_direct_via_cols)

    #     # samples = min(samples_direct, samples_via_reception)

    #     # Samples from Monte Carlo simulation
    #     # The essence is the same as the formula above, but the specific performance is obtained from the high-volume simulation.
    #     # Doubt the coupon bound formula is appropriate
    #     samples_via_reception = samples_from_reception(reception/codeword_len, codeword_len)
    #     samples = samples_via_reception
        
    #     return Code(
    #         size_msg_symbol=self.size_msg_symbol,
    #         msg_len=self.msg_len * col.msg_len,
    #         size_code_symbol=self.size_code_symbol,
    #         codeword_len=codeword_len,
    #         reception=reception,
    #         samples=samples
    #     )

    # Two dimension LT sampling for identify code and RS code
    def ltextend(self, col):
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
        
        # c is a constant and should be lager than 1. 
        # t=cnm.
        c = 1.2
        d=c
        n = max(self.codeword_len, col.codeword_len)
        k = min(self.codeword_len, col.codeword_len)

        # samples = c*n*k*ln(k/\delta)
         

        
        samples=n * samples_from_reception_LT(SECPAR_SOUND,k,n) + SECPAR_SOUND
       
        #print("k=",k,"c * math.sqrt(k) * math.log(k / (2**(-SECPAR_SOUND))) ** 2=",c * math.sqrt(k) * math.log2(k / (2**(-SECPAR_SOUND))),"d * math.sqrt(k) * math.log(n / k)=",d * math.sqrt(k) * math.log(n / k))
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

def samples_from_reception(sec_par, reception, codeword_len):
    '''
    Compute the number of samples needed to reconstruct
    data with probability at least 1 - 2^(-sec_par) based on
    the reception efficiency and a generalized coupon collector.
    Note: this may not be the tightest for all schemes (e.g. Tensor).
    '''
    # special case: if only one symbol is needed, we are done
    if reception == 1:
        return 1

    # special case: if all symbols are needed: just regular coupon collector
    if reception == codeword_len:
        n = codeword_len
        s = math.ceil((n / math.log(math.e, 2)) * (math.log(n, 2) + sec_par))
        return int(s)
#     n：代表码字的总符号数。
# math.log(math.e, 2)：计算自然对数 
# log2𝑒
#​
#  e，它是将自然对数转换为以 2 为底的对数所需的比例因子。数值约为 1.4427。
# math.log(n, 2)：计算 
# log2𝑛

#  n，表示以 2 为底的 

# n 的对数，是衡量收集 

# n 个不同符号所需的样本量的主要成分。
# sec_par：安全参数，用于调整所需的样本数，使数据重建的失败概率降低到 
# 2−sec_par
#  。这是一个额外的偏移量，确保样本数足够大以满足安全需求。
# math.ceil()：向上取整函数，确保样本数是整数。
    # generalized coupon collector
    delta = reception - 1
    c = delta / codeword_len
    s = math.ceil(-sec_par / math.log2(c) + (1.0 - math.log(math.e, c)) * delta)
# -sec_par / math.log2(c)：
# 这一项用于计算为了达到预期的安全性（即低失败概率），在 c 比例下所需的样本数。
# math.log2(c) 是以 2 为底的𝑐的对数。当 𝑐<1 时，该值为负，使得整个分式为正，表示需要更多的样本来确保重建的成功概率。(1.0 - math.log(math.e, c)) * delta：这是一个修正项，用于考虑恢复所需符号的数量。
# math.log(math.e, c) 是 c 的自然对数（以 e 为底）。
# 1.0 - math.log(math.e, c) 调整了对 delta 的放大或缩小效果，用于反映在给定比例 c 下恢复数据的难度。
# math.ceil()：向上取整，确保返回的样本数是整数。这是必要的，因为样本数量必须是整数才能在实际应用中使用。
    return int(s)


# def samples_from_reception(k_n, n):
#     k_n = float(f"{k_n:.2f}")
#     df = pd.read_csv(f"./{k_n}/wr.csv", header=None)
#     print('k_n=', k_n, 'n=', n)
#     # 确保第一列数据类型为整数（根据需要）
#     df[0] = df[0].astype(int)
#     # 创建布尔掩码
#     mask = df.iloc[:, 0] == n
#     # 提取对应的样本值
#     samples = df.loc[mask, 1].tolist()
#     print('samples:', samples)
#     # 返回样本值
#     return samples[0] 

#2024.11.14.12 lin
# def samples_from_reception_LT(sec_par,reception):
#     if reception <= 0 or sec_par <= 0:
#         raise ValueError("k 和 δ 必须为正数")
#     # print(math.log(reception / 2**(-sec_par)))
#     R=calculate_R(reception,sec_par)
#     H=harmonic_sum_modified(reception/R)
#     samples=reception+R*H+R*math.log(R/(2**(-sec_par)))
#     # print(R)
#     # print(H)
#     # print(samples)
#     return samples
def samples_from_reception_LT(sec_par,k,n):
    samples=0
    if k/n==1:
        samples=k+5.422*math.log(k)-32.139+sec_par
    elif k/n==0.75:
        samples_1=k+5.422*math.log(k)-32.139+sec_par
        samples=0.8617*samples_1 - 20.57+sec_par
    elif k/n==0.5:
        samples_1=k+5.422*math.log(k)-32.139+sec_par
        samples=n=0.7095*samples_1+ 29.541+sec_par
    return samples
# def samples_from_reception_LT(k_n, n):
#     k_n = float(f"{k_n:.2f}")
#     df = pd.read_csv(f"./{k_n}/ltcode_bp.csv", header=None)
#     # print('k_n=', k_n, 'n=', n)
#     # 确保第一列数据类型为整数（根据需要）
#     df[0] = df[0].astype(int)
#     # 创建布尔掩码
#     mask = df.iloc[:, 0] == n
#     # n
#     samples = df.loc[mask, 1].tolist()
#     # print('samples:', samples)
#     # 返回样本值
#     return samples[0] 


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
        samples=samples_from_reception(SECPAR_SOUND, k, k)
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
         samples=samples_from_reception(SECPAR_SOUND, k, n)
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
        samples=samples_from_reception_LT(SECPAR_SOUND, k,n)
    )
#=204.94+1.24x+8.85×(10^−6)(x^2)
# tests
# assert makeRSCode (5 , 2, 4) . tensor ( makeRSCode (5 , 2 , 4) ). reception == 8
# assert makeRSCode (5 , 2, 4) . reception == 2