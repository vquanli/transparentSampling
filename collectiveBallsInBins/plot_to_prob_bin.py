import matplotlib.pyplot as plt
import pandas as pd
import os
class_value = ['1024_256','1024_512','1024_768','2048_512','2048_1024','2048_1536']
# 读取CSV文件
for floder in class_value :
    file_names = ["wr.csv", "wor_32.csv", "wor_8.csv", "seg_32.csv", "seg_8.csv"]

    plt.figure(figsize=(10, 6))

    for file_name in file_names:
        # 读取CSV文件
        df = pd.read_csv( floder+'/'+file_name, header=None)
        
        # 提取数据
        x = df[0].values
        y = df[1].values

        # 绘制折线图
        plt.plot(x, y, label=file_name)

    # 添加标题和标签
    plt.title('N, K='+floder)
    plt.xlabel('Samples L · Q')
    plt.ylabel('Failure Probability p')

    # 添加图例
    plt.legend()
    # 保存图像
    plt.savefig(os.path.join(f'K-N={floder}.png'))
    # 显示图形
    plt.show()