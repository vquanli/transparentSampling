import os
import pandas as pd
import matplotlib.pyplot as plt


# Load the uploaded CSV files using f-string formatting to include kn value in the path
fri_com = pd.read_csv(f'csvdata/fri_comm_pq.csv')
hash_com = pd.read_csv(f'csvdata/hash_comm_pq.csv')
homhash_com = pd.read_csv(f'csvdata/homhash_comm_pq.csv')
rs_com = pd.read_csv(f'csvdata/rs_comm_pq.csv')
merkle_com = pd.read_csv(f'csvdata/merkle_comm_pq.csv')
tensor_com = pd.read_csv(f'csvdata/tensor_comm_pq.csv')
# lt_com = pd.read_csv(f'csvdata/{kn}/lt_comm_pq.csv')
tensorRSIdentity_com = pd.read_csv(f'csvdata/tensorRSIdentity_comm_pq.csv')
tensorLTIdentity_com = pd.read_csv(f'csvdata/tensorLTIdentity_comm_pq.csv')

# Renaming the columns for consistency
fri_com.columns = ['D', 'Query']
hash_com.columns = ['D', 'Query']
homhash_com.columns = ['D', 'Query']
rs_com.columns = ['D', 'Query']
merkle_com.columns = ['D', 'Query']
tensor_com.columns = ['D', 'Query']
# lt_com.columns = ['D', 'Query']
tensorRSIdentity_com.columns = ['D', 'Query']
tensorLTIdentity_com.columns = ['D', 'Query']

# Plotting the data
plt.figure(figsize=(12, 8))

# Plot each dataset with different marker shapes and colors
plt.plot(fri_com['D'], fri_com['Query'], marker='x', linestyle='-', color='red', label='FRI')             # 'x' marker, red color
# plt.plot(hash_com['D'], hash_com['Query'], marker='o', linestyle='-', color='blue', label='Hash')          # 'o' marker, blue color
# plt.plot(homhash_com['D'], homhash_com['Query'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
plt.plot(rs_com['D'], rs_com['Query'], marker='^', linestyle='-', color='purple', label='RS')              # '^' marker, purple color
plt.plot(tensor_com['D'], tensor_com['Query'], marker='d', linestyle='-', color='orange', label='Tensor')  # 'd' marker, orange color
# plt.plot(lt_com['D'], lt_com['Query'], marker='p', linestyle='-', color='brown', label='LT')               # 'p' marker, brown color
plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Query'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Query'], marker='*', linestyle='-', color='magenta', label='Tensor LT Identity') # '*' marker, magenta color
plt.plot(merkle_com['D'], merkle_com['Query'], marker='p', linestyle='-', color='brown', label='Merkle') 
# Set the style of the plot
plt.xlabel('D = |data| [MB]')
plt.ylabel('Query [KB]')

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()



# Save the plot and show it
plt.savefig('figs/comm_comparison_plot.pdf')
plt.show()
