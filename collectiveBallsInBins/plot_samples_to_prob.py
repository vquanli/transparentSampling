import matplotlib.pyplot as plt
import pandas as pd
import os

files_value = ['2048_1024', '2048_1536']
class_value = ['2048_1024', '2048_1536']
title_list = ['K=1024, N=2048', 'K=1536, N=2048']
marker_list = ['*', 'o', ' ', 'o', '*', 'd', 'o', 'v', 
               '^', '<', '>', 's', 'p', '*', 'h', 'D']
color_list = ['k', 'deepskyblue', 'r', 'k', 'r',
              'coral', 'orange', 'palegreen', 'deepskyblue',
              'lightsteelblue', 'navy', 'blueviolet', 'pink']
# label_list = ['With Replacement', 'LT Code With Gaussian', 'LT Code With BP']
label_list = ['With Replacement', 'LT Code']

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14  # Set default font size for better readability
# 读取CSV文件
for folder in files_value:
    # file_names = ["wr.csv", "LTgs.csv", "LTbp.csv"]
    file_names = ["wr.csv", "LTgs.csv"]
    plt.figure(figsize=(8, 6))
    i = 0
    for file_name in file_names:
        
        # 读取CSV文件
        df = pd.read_csv(folder + '/' + file_name, header=None)
        
        # 提取数据
        x = df[0].values
        y = df[1].values
        
        # 绘制折线图
        plt.plot(x, y, label=label_list[i], c=color_list[i], marker=marker_list[i])
        i += 1

    # 添加标题和标签
    plt.xlabel('Samples', fontdict={'family': 'Times New Roman', 'size': 20})
    plt.ylabel('Failure Probability', fontdict={'family': 'Times New Roman', 'size': 20})
    
    # 显示网格线
    plt.grid(True, which='both', linestyle=':', linewidth=0.5)

    # 设置图例标签的字体
    plt.legend(prop={'family': 'Times New Roman', 'size': 18})
    plt.yticks(fontsize=22)

# 设置x轴刻度字体大小
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    # 保存图像为PDF
    plt.savefig(os.path.join(f'LTBinBallFigs20241114\K-N={folder}.pdf'))  # 修改这里

    # 显示图形
    plt.show()
