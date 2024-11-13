import os
import pandas as pd
import matplotlib.pyplot as plt

k_n = ["K_N=1", "K_N=0.75", "K_N=0.5"]
for kn in k_n:
    # Load the uploaded CSV files, 使用 f-string 格式化字符串路径
    # fri_com = pd.read_csv(f'csvdata/{kn}/fri_com.csv')
    # hash_com = pd.read_csv(f'csvdata/{kn}/hash_com.csv')
    # homhash_com = pd.read_csv(f'csvdata/{kn}/homhash_com.csv')
    rs_com = pd.read_csv(f'csvdata/{kn}/rs_com.csv')
    # tensor_com = pd.read_csv(f'csvdata/{kn}/tensor_com.csv')
    lt_com = pd.read_csv(f'csvdata/{kn}/lt_com.csv')
    # tensorRSIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorRSIdentity_com.csv')
    # tensorLTIdentity_com = pd.read_csv(f'csvdata/{kn}/tensorLTIdentity_com.csv')

    # Renaming the columns for consistency
    # fri_com.columns = ['D', 'Commitment']
    # hash_com.columns = ['D', 'Commitment']
    # homhash_com.columns = ['D', 'Commitment']
    rs_com.columns = ['D', 'Commitment']
    # tensor_com.columns = ['D', 'Commitment']
    lt_com.columns = ['D', 'Commitment']
    # tensorRSIdentity_com.columns = ['D', 'Commitment']
    # tensorLTIdentity_com.columns = ['D', 'Commitment']

    # Plotting the data
    plt.figure(figsize=(12, 8))

    # Plot each dataset with different marker shapes and colors
    # plt.plot(fri_com['D'], fri_com['Commitment'], marker='x', linestyle='-', color='red', label='FRI')             # 'x' marker, red color
    # plt.plot(hash_com['D'], hash_com['Commitment'], marker='o', linestyle='-', color='blue', label='Hash')          # 'o' marker, blue color
    # plt.plot(homhash_com['D'], homhash_com['Commitment'], marker='s', linestyle='-', color='green', label='HomHash') # 's' marker, green color
    plt.plot(rs_com['D'], rs_com['Commitment'], marker='^', linestyle='-', color='purple', label='RS')              # '^' marker, purple color
    # plt.plot(tensor_com['D'], tensor_com['Commitment'], marker='d', linestyle='-', color='orange', label='Tensor')  # 'd' marker, orange color
    plt.plot(lt_com['D'], lt_com['Commitment'], marker='p', linestyle='-', color='brown', label='LT')               # 'p' marker, brown color
    # plt.plot(tensorRSIdentity_com['D'], tensorRSIdentity_com['Commitment'], marker='h', linestyle='-', color='cyan', label='Tensor RS Identity') # 'h' marker, cyan color
    # plt.plot(tensorLTIdentity_com['D'], tensorLTIdentity_com['Commitment'], marker='*', linestyle='-', color='magenta', label='Tensor LT Identity') # '*' marker, magenta color

    # Set the style of the plot
    plt.xlabel('D = |data| [MB]')
    plt.ylabel('Commitment [MB]')
    plt.title(f'{kn}')  # Update the title dynamically for each plot
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    # Make sure output directory exists
    output_dir = f'figs/{kn}'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot and show it
    plt.savefig(f'{output_dir}/com_comparison_plot_{kn}.pdf')
    plt.show()
