import matplotlib.pyplot as plt
import numpy as np

# Data
operations = ["Addition", "Subtraction", "Multiplication"]
methods = ["Ours", "Subword Tokenization", "Digitwise Tokenization"]
training_data = np.array([
    [6400, 409600, 409600],  # Addition
    [6400, np.nan, 720000],  # Subtraction
    [204800,  np.nan, np.nan]  # Multiplication (Not Achievable for Subword Tokenization)
])

# Define colors (matches legend)
academic_colors = ["#D62728", "#ADD8E6", "#808080"]  # Red, Light Blue, Grey

# Assign a more reasonable high placeholder value
high_placeholder = 10 * np.nanmax(training_data)  # Set "Not Achievable" bars to 10× max real value
training_data_nan_masked = np.nan_to_num(training_data, nan=high_placeholder)

# Plot settings
x = np.arange(len(operations))  # The label locations
width = 0.25  # Width of the bars

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Bars for each method with custom colors
bars = []
for i, (method, color) in enumerate(zip(methods, academic_colors)):
    y_values = training_data_nan_masked[:, i]
    bars.append(ax.bar(x + i * width - width, y_values, width, label=method, color=color))

# Function to add numerical values on top of bars

def autolabel_bars(rects, y_values, color):
    for rect, y in zip(rects, y_values):
        if y != high_placeholder:  # Normal values
            ax.text(
                rect.get_x() + rect.get_width() / 2, 
                y + 0.04 * 509600,  # Adjust position slightly above bar
                f"{int(y):,}", 
                ha='center', va='bottom', fontsize=8, fontweight='bold', color=color
            )

# Function to label 'Not Achievable' inside the bar

def autolabel_nan_bars(rects, y_values):
    for rect, y in zip(rects, y_values):
        if y == high_placeholder:  # Only apply to "Not Achievable" cases
            ax.text(
                rect.get_x() + rect.get_width() / 2, 
                809600 / 2,  # Position in middle of the bar
                "Not\nAchievable", 
                ha='center', va='center', fontsize=8, color='black', fontweight='bold'
            )

# Add labels to bars (FNE data in red, others in black)
for i, color in enumerate(academic_colors):
    text_color = "red" if i == 0 else "black"  # Make FNE labels red
    autolabel_bars(bars[i], training_data_nan_masked[:, i], text_color)
    autolabel_nan_bars(bars[i], training_data_nan_masked[:, i])

# Labels and formatting
# ax.set_xlabel("Operation", fontsize=15)
ax.set_ylabel("Training Data Needed (>99% Acc.)", fontsize=16)  # Compact and larger font
ax.set_title("Training Data Required to Achieve >99% Accuracy", fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(operations, fontsize=14)
ax.legend(fontsize=12)

# Adjust y-axis limit dynamically
ax.set_ylim(0, 1.2 * np.nanmax(training_data_nan_masked[training_data_nan_masked != high_placeholder]))  

# Show plot
plt.show()

# Save the figure
plt.savefig("data_comparison.png", dpi=300, bbox_inches='tight')
