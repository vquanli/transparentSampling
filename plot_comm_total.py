import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV files
fri_com = pd.read_csv('csvdata/fri_comm_total.csv')
hash_com = pd.read_csv('csvdata/hash_comm_total.csv')
homhash_com = pd.read_csv('csvdata/homhash_comm_total.csv')
rs_com = pd.read_csv('csvdata/rs_comm_total.csv')
tensor_com = pd.read_csv('csvdata/tensor_comm_total.csv')
lt_com = pd.read_csv('csvdata/lt_comm_total.csv')
# Renaming the columns for consistency
fri_com.columns = ['D', 'Total']
hash_com.columns = ['D', 'Total']
homhash_com.columns = ['D', 'Total']
rs_com.columns = ['D', 'Total']
tensor_com.columns = ['D', 'Total']
lt_com.columns = ['D', 'Total']
# Plotting the data
plt.figure(figsize=(10, 6))

# Plot each dataset with different marker shapes
plt.plot(fri_com['D'], fri_com['Total'], marker='x', linestyle='-', color='red', label='FRI')        # 'x' marker
plt.plot(hash_com['D'], hash_com['Total'], marker='o', linestyle='-', color='blue', label='Hash')     # 'o' marker
plt.plot(homhash_com['D'], homhash_com['Total'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker
plt.plot(rs_com['D'], rs_com['Total'], marker='^', linestyle='-', color='purple', label='RS')         # '^' marker
plt.plot(tensor_com['D'], tensor_com['Total'], marker='d', linestyle='-', color='orange', label='Tensor')   # 'd' marker
plt.plot(lt_com['D'], lt_com['Total'], marker='x', linestyle='-', color='orange', label='LT')   # 'd' marker
# Set the style of the plot
plt.xlabel('D = |data| [MB]')
plt.ylabel('Total [GB]')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
plt.savefig('comm_total_comparison_plot.pdf')
