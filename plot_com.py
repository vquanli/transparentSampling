import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV files, 使用 f-string 格式化字符串路径
fri_com = pd.read_csv(f'csvdata/fri_com.csv')
hash_com = pd.read_csv(f'csvdata/hash_com.csv')
homhash_com = pd.read_csv(f'csvdata//homhash_com.csv')
rs_com = pd.read_csv(f'csvdata/rs_com.csv')
tensor_com = pd.read_csv(f'csvdata/tensor_com.csv')
merkle_com = pd.read_csv(f'csvdata/merkle_com.csv')
# lt_com = pd.read_csv(f'csvdata/{kn}/lt_com.csv')
tensorRSIdentity_com = pd.read_csv(f'csvdata/tensorRSIdentity_com.csv')
tensorLTIdentity_com = pd.read_csv(f'csvdata/tensorLTIdentity_com.csv')

# Renaming the columns for consistency
fri_com.columns = ['D', 'Commitment']
hash_com.columns = ['D', 'Commitment']
homhash_com.columns = ['D', 'Commitment']
rs_com.columns = ['D', 'Commitment']
tensor_com.columns = ['D', 'Commitment']
merkle_com.columns = ['D', 'Commitment']
# lt_com.columns = ['D', 'Commitment']
tensorRSIdentity_com.columns = ['D', 'Commitment']
tensorLTIdentity_com.columns = ['D', 'Commitment']

# Set global font properties to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14  # Set default font size

# Plotting the data
plt.figure(figsize=(8, 6))

# Plot each dataset with different marker shapes and colors
plt.plot(fri_com['D'], fri_com['Commitment'], marker='d', linestyle='-', color='blue', label='FRIDA')             # 'x' marker, red color
plt.plot(hash_com['D'], hash_com['Commitment'], marker='^', linestyle='-', color='green', label='Hash')          # 'o' marker, blue color
# plt.plot(homhash_com['D'], homhash_com['Commitment'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
# plt.plot(rs_com['D'], rs_com['Commitment'], marker='^', linestyle='-', color='purple', label='RS')              # '^' marker, purple color
plt.plot(tensor_com['D'], tensor_com['Commitment'], marker='x', linestyle='-', color='red', label='Tensor', markeredgewidth=2)      # Change line to dashed
# plt.plot(lt_com['D'], lt_com['Commitment'], marker='p', linestyle='-', color='brown', label='LT')               # 'p' marker, brown color
# plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Commitment'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Commitment'], linestyle='-', color='#614099', label='TDAS', markerfacecolor='none') # Change shape to hollow circle
# plt.plot(merkle_com['D'], merkle_com['Commitment'], marker='p', linestyle='-', color='brown', label='Merkle')   

# Set the style of the plot
# plt.xlabel('D = |data| [MB]', fontsize=18)  # Increase font size for x label
plt.xlabel('N/K',fontsize=18)
plt.ylabel('Commitment [MB]', fontsize=18)  # Increase font size for y label
plt.xticks(fontsize=22)  # Increase font size for x-axis ticks
plt.yticks(fontsize=22)  # Increase font size for y-axis ticks
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)  # Increase font size for legend
plt.tight_layout()

# Save the plot and show it
plt.savefig('figs/com_comparison_plot.pdf')
plt.show()
