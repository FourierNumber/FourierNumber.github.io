import matplotlib.pyplot as plt
import numpy as np

# Set a professional font style
plt.rcParams["font.family"] = "DejaVu Sans"  # Change to "Times New Roman" if preferred

# Data
operations = ["Addition", "Subtraction", "Multiplication"]
methods = ["Ours", "Subword Tokenization", "Digitwise Tokenization"]
training_data = np.array([
    [6400, 409600, 409600],  # Addition
    [6400, np.nan, 720000],  # Subtraction
    [204800, np.nan, np.nan]  # Multiplication (Not Achievable for Subword Tokenization)
])

# Define colors (matches legend)
academic_colors = ["#D62728", "#1F77B4", "#808080"]  # Red, Blue, Grey

# Assign a high placeholder value for "Not Achievable"
high_placeholder = 10 * np.nanmax(training_data)
training_data_nan_masked = np.nan_to_num(training_data, nan=high_placeholder)

# Plot settings
x = np.arange(len(operations))
width = 0.25  

# Create figure with improved font and spacing
fig, ax = plt.subplots(figsize=(10, 6))

# Bars for each method with custom colors
bars = []
for i, (method, color) in enumerate(zip(methods, academic_colors)):
    y_values = training_data_nan_masked[:, i]
    bars.append(ax.bar(x + i * width - width, y_values, width, label=method, color=color, edgecolor='black'))

# Function to add numerical values on top of bars
def autolabel_bars(rects, y_values, color):
    for rect, y in zip(rects, y_values):
        if y != high_placeholder:
            ax.text(
                rect.get_x() + rect.get_width() / 2, 
                y + 0.03 * np.nanmax(training_data),  
                f"{int(y):,}", 
                ha='center', va='bottom', fontsize=8, fontweight='bold', color=color
            )

# Function to label 'Not Achievable' inside the bar
def autolabel_nan_bars(rects, y_values):
    for rect, y in zip(rects, y_values):
        if y == high_placeholder:
            ax.text(
                rect.get_x() + rect.get_width() / 2, 
                np.nanmax(training_data) / 2,  
                "Not\nAchievable", 
                ha='center', va='center', fontsize=6, color='white', fontweight='bold', bbox=dict(facecolor='black', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.3')
            )

# Add labels to bars
for i, color in enumerate(academic_colors):
    text_color = "red" if i == 0 else "black"
    autolabel_bars(bars[i], training_data_nan_masked[:, i], text_color)
    autolabel_nan_bars(bars[i], training_data_nan_masked[:, i])

# Labels and formatting
ax.set_ylabel("Training Data Needed (>99% Acc.)", fontsize=14, fontweight="bold")
ax.set_title("Training Data Required to Achieve >99% Accuracy", fontsize=16, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(operations, fontsize=12, fontweight="bold")

# Grid for better readability
ax.yaxis.grid(True, linestyle="dashed", alpha=0.5)
ax.set_axisbelow(True)

# Adjust y-axis limit dynamically
ax.set_ylim(0, 1.2 * np.nanmax(training_data_nan_masked[training_data_nan_masked != high_placeholder]))

# Adjust legend
ax.legend(fontsize=12, frameon=True, edgecolor='black')

# Show plot
plt.show()

# Save the figure
plt.savefig("data_comparison.png", dpi=300, bbox_inches='tight')
