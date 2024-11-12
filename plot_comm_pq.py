import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV files
fri_com = pd.read_csv('csvdata/fri_comm_pq.csv')
hash_com = pd.read_csv('csvdata/hash_comm_pq.csv')
homhash_com = pd.read_csv('csvdata/homhash_comm_pq.csv')
rs_com = pd.read_csv('csvdata/rs_comm_pq.csv')
tensor_com = pd.read_csv('csvdata/tensor_comm_pq.csv')
lt_com = pd.read_csv('csvdata/lt_comm_pq.csv')
# Renaming the columns for consistency
fri_com.columns = ['D', 'Query']
hash_com.columns = ['D', 'Query']
homhash_com.columns = ['D', 'Query']
rs_com.columns = ['D', 'Query']
tensor_com.columns = ['D', 'Query']
lt_com.columns = ['D', 'Query']
# Plotting the data
plt.figure(figsize=(10, 6))

# Plot each dataset with different marker shapes
plt.plot(fri_com['D'], fri_com['Query'], marker='x', linestyle='-', color='red', label='FRI')        # 'x' marker
plt.plot(hash_com['D'], hash_com['Query'], marker='o', linestyle='-', color='blue', label='Hash')     # 'o' marker
plt.plot(homhash_com['D'], homhash_com['Query'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker
plt.plot(rs_com['D'], rs_com['Query'], marker='^', linestyle='-', color='purple', label='RS')         # '^' marker
plt.plot(tensor_com['D'], tensor_com['Query'], marker='d', linestyle='-', color='orange', label='Tensor')   # 'd' marker
plt.plot(lt_com['D'], lt_com['Query'], marker='x', linestyle='-', color='orange', label='LT')   # 'd' marker
# Set the style of the plot
plt.xlabel('D = |data| [MB]')
plt.ylabel('Query [KB]')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
plt.savefig('comm_comparison_plot.pdf')
