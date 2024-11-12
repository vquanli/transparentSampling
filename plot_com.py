import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV files
fri_com = pd.read_csv('csvdata/fri_com.csv')
hash_com = pd.read_csv('csvdata/hash_com.csv')
homhash_com = pd.read_csv('csvdata/homhash_com.csv')
rs_com = pd.read_csv('csvdata/rs_com.csv')
tensor_com = pd.read_csv('csvdata/tensor_com.csv')
lt_com = pd.read_csv('csvdata/lt_com.csv')
# Renaming the columns for consistency
fri_com.columns = ['D', 'Commitment']
hash_com.columns = ['D', 'Commitment']
homhash_com.columns = ['D', 'Commitment']
rs_com.columns = ['D', 'Commitment']
tensor_com.columns = ['D', 'Commitment']
lt_com.columns = ['D', 'Commitment']
# Plotting the data
plt.figure(figsize=(10, 6))

# Plot each dataset with different marker shapes
plt.plot(fri_com['D'], fri_com['Commitment'], marker='x', linestyle='-', color='red', label='FRI')        # 'x' marker
plt.plot(hash_com['D'], hash_com['Commitment'], marker='o', linestyle='-', color='blue', label='Hash')     # 'o' marker
plt.plot(homhash_com['D'], homhash_com['Commitment'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker
plt.plot(rs_com['D'], rs_com['Commitment'], marker='^', linestyle='-', color='purple', label='RS')         # '^' marker
plt.plot(tensor_com['D'], tensor_com['Commitment'], marker='d', linestyle='-', color='orange', label='Tensor')   # 'd' marker
plt.plot(lt_com['D'], lt_com['Commitment'], marker='x', linestyle='-', color='orange', label='LT')   # 'd' marker
# Set the style of the plot
plt.xlabel('D = |data| [MB]')
plt.ylabel('Commitment [MB]')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
plt.savefig('com_comparison_plot.pdf')
