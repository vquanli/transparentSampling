import matplotlib.pyplot as plt
import pandas as pd
import os

files_value = ['0_5', '0_75', '1']
class_value = ['0.5', '0.75', '1']
marker_list = ['o', '*','d','v','^', '<', '>', 's', 'p', '*', 'h', 'D']
color_list = ['k', 'palegreen','deepskyblue', 'coral','blueviolet','coral', 'orange', 'palegreen', 'deepskyblue', 'lightsteelblue', 'navy', 'blueviolet', 'pink']
# label_list=['With Replacement','LT Code With Guassian','LT Code With BP']
label_list=['With Replacement','LT Code With Guassian','LT Code With BP']
# Create a figure with subplots, including an extra one for the legend
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(18, 12))
axes = axes.flatten()

# Iterate through each folder and subplot
for j, (floder, ax) in enumerate(zip(files_value, axes[:3])):
    file_names = ["wr.csv", "ltcode_gs.csv","ltcode_bp.csv"]
    
    for i, file_name in enumerate(file_names):
        # Read CSV file
        df = pd.read_csv(floder + '/' + file_name, header=None)
        
        # Extract data
        x = df[0].values
        y = df[1].values
        
        # Plot line graph on the current subplot
        ax.plot(x, y, label=label_list[i], c=color_list[i], marker=marker_list[i])

    # Add title and labels for each subplot
    ax.set_title(f'K/N={class_value[j]}', fontdict={'family': 'Times New Roman', 'size': 16})
    ax.set_xlabel('Number of Bins N', fontdict={'family': 'Times New Roman', 'size': 12})
    ax.set_ylabel('Samples L·Q', fontdict={'family': 'Times New Roman', 'size': 12})
    

# Add a legend to the fourth subplot
handles, labels = axes[0].get_legend_handles_labels()
legend = axes[3].legend(handles, labels, loc='center', fontsize=30)
axes[3].axis('off')  # Turn off the axis for the legend subplot

# Set font properties for legend labels
for text in legend.get_texts():
    text.set_fontname('Times New Roman')
    text.set_fontsize(30)

# Adjust layout
plt.tight_layout()

# Save and show the combined plot
plt.savefig('combined_subplots_with_legend.png')
plt.show()