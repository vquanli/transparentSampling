import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV files
fri_com = pd.read_csv(f'csvdata/fri_comm_total.csv')
hash_com = pd.read_csv(f'csvdata/hash_comm_total.csv')
homhash_com = pd.read_csv(f'csvdata/homhash_comm_total.csv')
rs_com = pd.read_csv(f'csvdata/rs_comm_total.csv')
merkle_com = pd.read_csv(f'csvdata/merkle_comm_total.csv')
tensor_com = pd.read_csv(f'csvdata/tensor_comm_total.csv')
lt_com = pd.read_csv(f'csvdata/lt_comm_total.csv')
tensorRSIdentity_com = pd.read_csv(f'csvdata/tensorRSIdentity_comm_total.csv')
tensorLTIdentity_com = pd.read_csv(f'csvdata/tensorLTIdentity_comm_total.csv')

# Renaming the columns for consistency
fri_com.columns = ['D', 'Total']
hash_com.columns = ['D', 'Total']
homhash_com.columns = ['D', 'Total']
rs_com.columns = ['D', 'Total']
tensor_com.columns = ['D', 'Total']
lt_com.columns = ['D', 'Total']
tensorRSIdentity_com.columns = ['D', 'Total']
tensorLTIdentity_com.columns = ['D', 'Total']
merkle_com.columns = ['D', 'Total']

# Set global font properties to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14  # Set default font size for better readability

# Plotting the data
plt.figure(figsize=(8, 6))

# Plot each dataset with different marker shapes and colors
plt.plot(fri_com['D'], fri_com['Total'], marker='d', linestyle='-', color='blue', label='FRIDA')             # 'd' marker, blue color
plt.plot(hash_com['D'], hash_com['Total'], marker='^', linestyle='-', color='green', label='Hash')          # '^' marker, green color
# plt.plot(homhash_com['D'], homhash_com['Total'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
# plt.plot(rs_com['D'], rs_com['Total'], marker='^', linestyle='-', color='purple', label='RS')              # '^' marker, purple color
plt.plot(tensor_com['D'], tensor_com['Total'], marker='x', linestyle='-', color='red', label='Tensor',markeredgewidth=2)      # 'x' marker, red color
# plt.plot(lt_com['D'], lt_com['Total'], marker='p', linestyle='-', color='brown', label='LT')               # 'p' marker, brown color
# plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Total'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Total'], linestyle='-', color='#614099', label='TDAS') # '>' marker, magenta color
# plt.plot(merkle_com['D'], merkle_com['Total'], marker='p', linestyle='-', color='brown', label='Merkle')   

# Set the style of the plot
# plt.xlabel('D = |data| [MB]', fontsize=18)  # Increase font size for x-axis label
plt.xlabel('N/K',fontsize=18)
plt.ylabel('Total [GB]', fontsize=18)       # Increase font size for y-axis label
plt.xticks(fontsize=22)                     # Increase font size for x-axis ticks
plt.yticks(fontsize=22)                     # Increase font size for y-axis ticks
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)                     # Increase font size for legend
plt.tight_layout()

# Save the plot and show it
plt.savefig('figs/comm_total_comparison_plot.pdf')
plt.show()
