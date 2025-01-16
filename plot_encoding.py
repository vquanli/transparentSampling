import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV files using f-string formatting to include kn value in the path
fri_com = pd.read_csv(f'csvdata/fri_encoding.csv')
hash_com = pd.read_csv(f'csvdata/hash_encoding.csv')
homhash_com = pd.read_csv(f'csvdata/homhash_encoding.csv')
rs_com = pd.read_csv(f'csvdata/rs_encoding.csv')
tensor_com = pd.read_csv(f'csvdata/tensor_encoding.csv')
merkle_com = pd.read_csv(f'csvdata/merkle_encoding.csv')
lt_com = pd.read_csv(f'csvdata/lt_encoding.csv')
tensorRSIdentity_com = pd.read_csv(f'csvdata/tensorRSIdentity_encoding.csv')
tensorLTIdentity_com = pd.read_csv(f'csvdata/tensorLTIdentity_encoding.csv')

# Renaming the columns for consistency
fri_com.columns = ['D', 'Encoding']
hash_com.columns = ['D', 'Encoding']
homhash_com.columns = ['D', 'Encoding']
rs_com.columns = ['D', 'Encoding']
tensor_com.columns = ['D', 'Encoding']
lt_com.columns = ['D', 'Encoding']
tensorRSIdentity_com.columns = ['D', 'Encoding']
tensorLTIdentity_com.columns = ['D', 'Encoding']
merkle_com.columns = ['D', 'Encoding']

# Set global font properties to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14  # Set default font size for better readability

# Plotting the data
plt.figure(figsize=(8, 6))

# Plot each dataset with different marker shapes and colors
plt.plot(fri_com['D'], fri_com['Encoding'], marker='d', linestyle='-', color='blue', label='FRIDA')  # 'd' marker, red color
plt.plot(hash_com['D'], hash_com['Encoding'], marker='^', linestyle='-', color='green', label='Hash')  # '^' marker, blue color
# plt.plot(homhash_com['D'], homhash_com['Encoding'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
# plt.plot(rs_com['D'], rs_com['Encoding'], marker='^', linestyle='-', color='purple', label='RS') # '^' marker, purple color
plt.plot(tensor_com['D'], tensor_com['Encoding'], marker='x', linestyle='-', color='red', label='Tensor',markeredgewidth=2)  # 'x' marker, orange color
# plt.plot(lt_com['D'], lt_com['Encoding'], marker='p', linestyle='-', color='brown', label='LT') # 'p' marker, brown color
# plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Encoding'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Encoding'], linestyle='-', color='#614099', label='TDAS')  # '>' marker, magenta color
# plt.plot(merkle_com['D'], merkle_com['Encoding'], marker='p', linestyle='-', color='brown', label='Merkle') 

# Set the style of the plot
# plt.xlabel('D = |data| [MB]', fontsize=18)  # Increase font size for x-axis label
plt.xlabel('N/K',fontsize=18)
plt.ylabel('Commitment [MB]', fontsize=18)  # Increase font size for y-axis label
plt.xticks(fontsize=22)  # Increase font size for x-axis ticks
plt.yticks(fontsize=22)  # Increase font size for y-axis ticks
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=18)  # Control legend font size
plt.tight_layout()

# Save the plot and show it
output_dir = 'figs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.savefig(f'{output_dir}/encoding_comparison_plot.pdf')
plt.show()
