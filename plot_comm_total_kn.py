import os
import pandas as pd
import matplotlib.pyplot as plt

k_n = ["K_N=1", "K_N=0.75", "K_N=0.5"]
for kn in k_n:
    # Load the uploaded CSV files
    fri_com = pd.read_csv(f'csvdata/{kn}/fri_comm_total.csv')
    hash_com = pd.read_csv(f'csvdata/{kn}/hash_comm_total.csv')
    homhash_com = pd.read_csv(f'csvdata/{kn}/homhash_comm_total.csv')
    rs_com = pd.read_csv(f'csvdata/{kn}/rs_comm_total.csv')
    merkle_com = pd.read_csv(f'csvdata/{kn}/merkle_comm_total.csv')
    tensor_com = pd.read_csv(f'csvdata/{kn}/tensor_comm_total.csv')
    lt_com = pd.read_csv(f'csvdata/{kn}/lt_comm_total.csv')
    tensorRSIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorRSIdentity_comm_total.csv')
    tensorLTIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorLTIdentity_comm_total.csv')

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
    # Plotting the data
    plt.figure(figsize=(12, 8))

    # Plot each dataset with different marker shapes and colors
    # plt.plot(fri_com['D'], fri_com['Total'], marker='x', linestyle='-', color='red', label='FRI')             # 'x' marker, red color
    # plt.plot(hash_com['D'], hash_com['Total'], marker='o', linestyle='-', color='blue', label='Hash')          # 'o' marker, blue color
    # plt.plot(homhash_com['D'], homhash_com['Total'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
    # plt.plot(rs_com['D'], rs_com['Total'], marker='^', linestyle='-', color='purple', label='RS')              # '^' marker, purple color
    plt.plot(tensor_com['D'], tensor_com['Total'], marker='d', linestyle='-', color='orange', label='Tensor')  # 'd' marker, orange color
    # plt.plot(lt_com['D'], lt_com['Total'], marker='p', linestyle='-', color='brown', label='LT')               # 'p' marker, brown color
    plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Total'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
    plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Total'], marker='*', linestyle='-', color='magenta', label='Tensor LT Identity') # '*' marker, magenta color
    # plt.plot(merkle_com['D'], merkle_com['Total'], marker='p', linestyle='-', color='brown', label='Merkle') 
    # Set the style of the plot
    plt.xlabel('D = |data| [MB]')
    plt.ylabel('Total [GB]')
    plt.title(f'{kn}')  # Update the title dynamically for each plot
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    # Make sure output directory exists
    output_dir = f'figs/{kn}'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot and show it
    plt.savefig(f'{output_dir}/comm_total_comparison_plot_{kn}.pdf')
    plt.show()
