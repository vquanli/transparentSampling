import os
import pandas as pd
import matplotlib.pyplot as plt
k_n = ["K_N=1", "K_N=0.75", "K_N=0.5"]
for kn in k_n:
    # Load the uploaded CSV files using f-string formatting to include kn value in the path
    fri_com = pd.read_csv(f'csvdata/{kn}/fri_encoding.csv')
    hash_com = pd.read_csv(f'csvdata/{kn}/hash_encoding.csv')
    homhash_com = pd.read_csv(f'csvdata/{kn}/homhash_encoding.csv')
    rs_com = pd.read_csv(f'csvdata/{kn}/rs_encoding.csv')
    tensor_com = pd.read_csv(f'csvdata/{kn}/tensor_encoding.csv')
    merkle_com = pd.read_csv(f'csvdata/{kn}/merkle_encoding.csv')
    lt_com = pd.read_csv(f'csvdata/{kn}/lt_encoding.csv')
    tensorRSIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorRSIdentity_encoding.csv')
    tensorLTIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorLTIdentity_encoding.csv')

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
    # Plotting the data
    plt.figure(figsize=(12, 8))

    # Plot each dataset with different marker shapes and colors
    plt.plot(fri_com['D'], fri_com['Encoding'], marker='x', linestyle='-', color='red', label='FRI')             # 'x' marker, red color
    # plt.plot(hash_com['D'], hash_com['Encoding'], marker='o', linestyle='-', color='blue', label='Hash')          # 'o' marker, blue color
    # plt.plot(homhash_com['D'], homhash_com['Encoding'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
    plt.plot(rs_com['D'], rs_com['Encoding'], marker='^', linestyle='-', color='purple', label='RS')              # '^' marker, purple color
    plt.plot(tensor_com['D'], tensor_com['Encoding'], marker='d', linestyle='-', color='orange', label='Tensor')  # 'd' marker, orange color
    # plt.plot(lt_com['D'], lt_com['Encoding'], marker='p', linestyle='-', color='brown', label='LT')               # 'p' marker, brown color
    plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Encoding'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
    plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Encoding'], marker='*', linestyle='-', color='magenta', label='Tensor LT Identity') # '*' marker, magenta color
    plt.plot(merkle_com['D'], merkle_com['Encoding'], marker='p', linestyle='-', color='brown', label='Merkle') 
    # Set the style of the plot
    plt.xlabel('D = |data| [MB]')
    plt.ylabel('Encoding [GB]')
    plt.title(f'{kn}')  # Update the title dynamically for each plot
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    # Make sure output directory exists
    output_dir = f'figs/{kn}'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot and show it
    plt.savefig(f'{output_dir}/encoding_comparison_plot_{kn}.pdf')
    plt.show()
