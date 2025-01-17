import os
import pandas as pd
import matplotlib.pyplot as plt

# 定义 k 值列表，与生成 CSV 文件时的 K 值保持一致
K = [1024, 2048, 4096]

# 初始化一个空的 DataFrame 列表，用于存储每个 k 的数据
data_frames = []

# 遍历每个 k 值，读取对应的 CSV 文件
for k in K:
    file_path = f'csvdata/hash_samples_k={k}.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.columns = ['s', 'samples (KB)']  # 重命名列名
        df['k'] = k  # 添加一列 k 值，便于区分
        data_frames.append(df)
    else:
        print(f"Warning: File {file_path} not found!")

# 合并所有 DataFrame
all_data = pd.concat(data_frames, ignore_index=True)

# 设置全局字体属性为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14  # 设置默认字体大小

# 绘图
plt.figure(figsize=(8, 6))

# 遍历每个 k 值的数据并绘制曲线
for k in K:
    subset = all_data[all_data['k'] == k]  # 筛选出当前 k 的数据
    
    # 根据 k 值设置不同的样式
    if k == 1024:
        plt.plot(
            subset['s'], 
            subset['samples (KB)'], 
            marker='d', linestyle='-', color='blue', label=f'K={k}'  # 蓝色，菱形标记
        )
    elif k == 2048:
        plt.plot(
            subset['s'], 
            subset['samples (KB)'], 
            marker='^', linestyle='-', color='green', label=f'K={k}'  # 绿色，三角形标记
        )
    elif k == 4096:
        plt.plot(
            subset['s'], 
            subset['samples (KB)'], 
            marker='x', linestyle='-', color='red', label=f'K={k}', markeredgewidth=2  # 红色，叉形标记
        )

# 设置图表样式
plt.xlabel('Log(N/K)', fontsize=18)
plt.ylabel('# of samples', fontsize=18)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)  # 图例字体大小
plt.tight_layout()

# 保存并展示图表
os.makedirs('figs', exist_ok=True)  # 如果目录不存在，则创建
plt.savefig('figs/hash_samples_comparison_plot.pdf')
plt.show()
