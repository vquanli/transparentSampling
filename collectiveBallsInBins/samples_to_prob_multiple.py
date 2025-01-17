import matplotlib.pyplot as plt
import pandas as pd

files_value = ['2048_1024','2048_1536']
class_value = ['2048_1024','2048_1536']
marker_list = ['o', '*','d','o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'D']
color_list = ['k', 'palegreen','deepskyblue','k', 'r', 'coral', 'orange', 'palegreen', 'deepskyblue', 'lightsteelblue', 'navy', 'blueviolet', 'pink']
title_list=['K=1024, N=2048','K=1536, N=2048']
label_list=['With Replacement','LT Code With Guassian','LT Code With BP']
# Create a figure with subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

# Iterate through each folder and subplot
for j, (floder, ax) in enumerate(zip(files_value, axes)):
    file_names = ["wr.csv","LTgs.csv","LTbp.csv"]
    
    for i, file_name in enumerate(file_names):
        # Read CSV file
        df = pd.read_csv(floder + '/' + file_name, header=None)
        
        # Extract data
        x = df[0].values
        y = df[1].values
        
        # Plot line graph on the current subplot
        ax.plot(x, y, label=label_list[i], c=color_list[i], marker=marker_list[i])

    # Add title and labels for each subplot
    ax.set_title(f'{title_list[j]}', fontdict={'family': 'Times New Roman', 'size': 16})
    ax.set_xlabel('Samples L·Q', fontdict={'family': 'Times New Roman', 'size': 12})
    ax.set_ylabel('Failure Probability', fontdict={'family': 'Times New Roman', 'size': 12})
    
    # Set font properties for legend
    legend = ax.legend()
    for text in legend.get_texts():
        text.set_fontname('Times New Roman')
        text.set_fontsize(12)

# Adjust layout
plt.tight_layout()

# Save and show the combined plot
plt.savefig('combined_subplots_FP.png')
plt.show()