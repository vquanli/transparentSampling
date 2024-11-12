import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV files
fri_com = pd.read_csv('csvdata/fri_encoding.csv')
hash_com = pd.read_csv('csvdata/hash_encoding.csv')
homhash_com = pd.read_csv('csvdata/homhash_encoding.csv')
rs_com = pd.read_csv('csvdata/rs_encoding.csv')
tensor_com = pd.read_csv('csvdata/tensor_encoding.csv')
lt_com = pd.read_csv('csvdata/lt_encoding.csv')
# Renaming the columns for consistency
fri_com.columns = ['D', 'Encoding']
hash_com.columns = ['D', 'Encoding']
homhash_com.columns = ['D', 'Encoding']
rs_com.columns = ['D', 'Encoding']
tensor_com.columns = ['D', 'Encoding']
lt_com.columns = ['D', 'Encoding']
# Plotting the data
plt.figure(figsize=(10, 6))

# Plot each dataset with different marker shapes
plt.plot(fri_com['D'], fri_com['Encoding'], marker='x', linestyle='-', color='red', label='FRI')        # 'x' marker
plt.plot(hash_com['D'], hash_com['Encoding'], marker='o', linestyle='-', color='blue', label='Hash')     # 'o' marker
plt.plot(homhash_com['D'], homhash_com['Encoding'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker
plt.plot(rs_com['D'], rs_com['Encoding'], marker='^', linestyle='-', color='purple', label='RS')         # '^' marker
plt.plot(tensor_com['D'], tensor_com['Encoding'], marker='d', linestyle='-', color='orange', label='Tensor')   # 'd' marker
plt.plot(lt_com['D'], lt_com['Encoding'], marker='x', linestyle='-', color='orange', label='LT')   # 'd' marker
# Set the style of the plot
plt.xlabel('D = |data| [MB]')
plt.ylabel('Encoding [GB]')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
plt.savefig('encoding_comparison_plot.pdf')
