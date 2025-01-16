import matplotlib.pyplot as plt
import pandas as pd
import os
files_value = ['0_5','0_75','1']
class_value = ['0.5','0.75','1']
marker_list = ['*', 'o',' ','o', 'v', 
               '^', '<', 
               '>', 's', 
               'p', '*', 
               'h', 'D',
              ]
color_list = ['k','deepskyblue','r','k', 'r',
             'coral', 'orange',
             'palegreen', 'deepskyblue',
             'lightsteelblue', 'navy',
             'blueviolet', 'pink']
label_list=['With Replacement','LT Code With Guassian','LT Code With BP']
#label_list=['With Replacement','LT Code']
# Set global font properties to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14  # Set default font size for better readability
# 读取CSV文件
for floder in files_value :
    file_names = ["wr.csv","ltcode_gs.csv","ltcode_bp.csv"]
    #file_names = ["wr.csv","ltcode_gs.csv"]
    plt.figure(figsize=(8, 6))
    i=0
    for file_name in file_names:
        
        # 读取CSV文件
        df = pd.read_csv( floder+'/'+file_name, header=None)
        
        # 提取数据
        x = df[0].values
        y = df[1].values
        plt.plot(x, y, label=label_list[i],c=color_list[i],marker=marker_list[i])
        # 绘制折线图
        # if i==2:
        #     plt.plot(x, y, label=label_list[i],c=color_list[i],marker=marker_list[i],linestyle="--")
        
        i=i+1
    # 添加标题和标签
    #plt.title('K/N='+class_value[j],fontdict={'family' : 'Times New Roman', 'size'   : 16})
    
    plt.xlabel('# of bins N',fontdict={'family' : 'Times New Roman', 'size'   : 20},fontsize=20)
    plt.ylabel('Samples',fontdict={'family' : 'Times New Roman', 'size'   : 20},fontsize=20)
    plt.grid(True, which='both', linestyle=':', linewidth=0.5)
    # Set font properties for legend labels
 # 设置图例标签的字体
    plt.legend(prop={'family': 'Times New Roman', 'size': 18})
# 设置y轴刻度字体大小
    plt.yticks(fontsize=22)

# 设置x轴刻度字体大小
    plt.xticks(fontsize=22)
    # 调整布局以防止文字被裁剪
    plt.tight_layout()
    # 保存图像
    plt.savefig(os.path.join(f'LTBinBallFigs20250105\K-N={floder}.pdf'))  # 修改这里
    # 显示图形
    plt.show()
