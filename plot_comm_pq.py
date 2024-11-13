import os
import pandas as pd
import matplotlib.pyplot as plt

k_n = ["K_N=1", "K_N=0.75", "K_N=0.5"]
for kn in k_n:
    # Load the uploaded CSV files using f-string formatting to include kn value in the path
    # fri_com = pd.read_csv(f'csvdata/{kn}/fri_comm_pq.csv')
    # hash_com = pd.read_csv(f'csvdata/{kn}/hash_comm_pq.csv')
    # homhash_com = pd.read_csv(f'csvdata/{kn}/homhash_comm_pq.csv')
    rs_com = pd.read_csv(f'csvdata/{kn}/rs_comm_pq.csv')
    # tensor_com = pd.read_csv(f'csvdata/{kn}/tensor_comm_pq.csv')
    lt_com = pd.read_csv(f'csvdata/{kn}/lt_comm_pq.csv')
    # tensorRSIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorRSIdentity_comm_pq.csv')
    # tensorLTIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorLTIdentity_comm_pq.csv')

    # Renaming the columns for consistency
    # fri_com.columns = ['D', 'Query']
    # hash_com.columns = ['D', 'Query']
    # homhash_com.columns = ['D', 'Query']
    rs_com.columns = ['D', 'Query']
    # tensor_com.columns = ['D', 'Query']
    lt_com.columns = ['D', 'Query']
    # tensorRSIdentity_com.columns = ['D', 'Query']
    # tensorLTIdentity_com.columns = ['D', 'Query']

    # Plotting the data
    plt.figure(figsize=(12, 8))

    # Plot each dataset with different marker shapes and colors
    # plt.plot(fri_com['D'], fri_com['Query'], marker='x', linestyle='-', color='red', label='FRI')             # 'x' marker, red color
    # plt.plot(hash_com['D'], hash_com['Query'], marker='o', linestyle='-', color='blue', label='Hash')          # 'o' marker, blue color
    # plt.plot(homhash_com['D'], homhash_com['Query'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
    plt.plot(rs_com['D'], rs_com['Query'], marker='^', linestyle='-', color='purple', label='RS')              # '^' marker, purple color
    # plt.plot(tensor_com['D'], tensor_com['Query'], marker='d', linestyle='-', color='orange', label='Tensor')  # 'd' marker, orange color
    plt.plot(lt_com['D'], lt_com['Query'], marker='p', linestyle='-', color='brown', label='LT')               # 'p' marker, brown color
    # plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Query'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
    # plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Query'], marker='*', linestyle='-', color='magenta', label='Tensor LT Identity') # '*' marker, magenta color

    # Set the style of the plot
    plt.xlabel('D = |data| [MB]')
    plt.ylabel('Query [KB]')
    plt.title(f'{kn}')  # Update the title dynamically for each plot
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    # Make sure output directory exists
    output_dir = f'figs/{kn}'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot and show it
    plt.savefig(f'{output_dir}/comm_comparison_plot_{kn}.pdf')
    plt.show()
