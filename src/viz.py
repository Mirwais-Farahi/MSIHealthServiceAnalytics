import matplotlib.pyplot as plt
import seaborn as sn

# visualize above table using bar chart
def plot_vertical_bar_chart(x_col, y_col, colors):
    """
    Function to plot a vertical bar chart using the given dataset and colors.

    Parameters:
        site_distribution (DataFrame): The dataset containing 'FACTYPE' and 'Total Surveys in Each Site'.
        colors (list): List of colors for the bars.
    
    Returns:
        None (Displays the plot).
    """
    # Create vertical bar chart
    ax = plt.bar(x_col, y_col, color=colors)

    # Remove border (spines) around the plot
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Add count/percentage labels on the bars
    for bar in ax:
        height = bar.get_height()  # For vertical bars, use height instead of width
        plt.text(bar.get_x() + bar.get_width()/2, height + 1, f"{height:.0f}",  # Adjust vertical position of text
                 ha='center', va='bottom', fontsize=12, color='black')

    # Formatting
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Show plot
    plt.show()

def plot_distribution(data, index, cols, values, colors):
    """
    Plots a clustered bar chart showing the distribution of facility types by region.
    
    Parameters:
    facility_types (DataFrame): A pandas DataFrame containing 'REGION', 'FACTYPE', and 'Count' columns.
    colors (list): A list of colors for the bars in the plot.
    """
    vis_facility_types = data.pivot(index=index, columns=cols, values=values)

    # Plotting the clustered bar chart with adjusted layout
    ax = vis_facility_types.plot(kind='bar', width=0.9, color=colors, edgecolor='none')

    # Adding count labels on top of each bar
    for bars in ax.containers:
        ax.bar_label(bars, fmt='%.0f', fontsize=10, padding=3)

    # Customizing the chart
    plt.xlabel('Region', fontsize=11)
    plt.xticks(rotation=0, ha='center', fontsize=10)
    plt.yticks(fontsize=10)

    # Removing the border around the chart (spines)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Adding a legend
    plt.legend(title='Facility Type', title_fontsize=11, fontsize=10)

    # Adding grid lines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Adjusting layout
    plt.tight_layout()

    # Show the plot
    plt.show()