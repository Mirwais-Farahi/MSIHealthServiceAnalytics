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

# Function to calculate percentage
def calculate_percentage(df, count_column):
    total = df[count_column].sum()
    df['Percentage'] = (df[count_column] / total) * 100
    return df

# Function to plot bar chart with percentage labels
def plot_bar_chart_with_percentage(data, category_column, count_column, colors):
    # Calculate the percentage using the provided count column
    data = calculate_percentage(data, count_column)
    
    # Create the horizontal bar plot
    ax = plt.barh(data[category_column], data['Percentage'], color=colors)

    # Remove border (spines) around the plot
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    # Add percentage labels on bars
    for bar in ax:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height()/2, f"{width:.1f}%",
                 ha='left', va='center', fontsize=12, color='black')

    plt.grid(axis='x', linestyle='-', alpha=0.07)
    plt.tight_layout()

    # Show the plot
    plt.show()