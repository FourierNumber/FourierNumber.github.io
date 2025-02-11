import matplotlib.pyplot as plt
import numpy as np

# Set a professional font style
plt.rcParams["font.family"] = "DejaVu Sans"  # Change to "Times New Roman" if preferred

# Methods
methods = ["Ours", "Digit-wise", "Subword"]

# Metrics for each method across different tasks
train_times = [3*60+18, 11*60+48, 6*60+46]  # Training times in seconds
test_times = [29, 85, 58]  # Testing times in seconds
tokens = [1, 7, 3]  # Tokens per method
accuracy_addition = [100, 99.85, 97.94]  # Accuracy in Decimal Addition

train_times_sub = [2*60+42, 9*60+41, 5*60+47]
test_times_sub = [29, 75, 54]
tokens_sub = [1, 5, 2]
accuracy_sub = [100, 99.71, 91.66]  # Accuracy in Subtraction

train_times_mul = [2*60+56, 10*60+11, 6*60+20]
test_times_mul = [33, 78, 58]
tokens_mul = [1, 8, 3]
accuracy_mul = [98.56, 81.21, 8.05]  # Accuracy in Multiplication

# Define new colors
academic_colors = ["#D62728", "#1F77B4", "#808080"]  # Red, Blue, Grey

# Redefining x-axis to group by dataset instead of method
datasets = ["Addition", "Subtraction", "Multiplication"]
x = np.arange(len(datasets))  # Label locations
width = 0.25  # Bar width (slightly smaller for better spacing)

# ----- Training Time Comparison -----
plt.figure(figsize=(10, 6))
plt.bar(x - width, [train_times[0], train_times_sub[0], train_times_mul[0]], width, label="Ours", color=academic_colors[0], edgecolor='black')
plt.bar(x, [train_times[1], train_times_sub[1], train_times_mul[1]], width, label="Digit-wise", color=academic_colors[1], edgecolor='black')
plt.bar(x + width, [train_times[2], train_times_sub[2], train_times_mul[2]], width, label="Subword", color=academic_colors[2], edgecolor='black')

# Formatting
plt.xticks(x, datasets, fontsize=12, fontweight='bold')
plt.ylabel("Training and Inference Time (Seconds)", fontsize=14, fontweight="bold")
plt.title("Comparison of Training and Inference Time per Epoch", fontsize=16, fontweight="bold")
plt.legend(fontsize=12, frameon=True, edgecolor='black')
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='dashed', alpha=0.5)  # Light grid for readability
plt.tight_layout()
plt.savefig("training_time_comparison.png", dpi=300, bbox_inches="tight")

# ----- Accuracy Comparison -----
plt.figure(figsize=(10, 6))
plt.bar(x - width, [accuracy_addition[0], accuracy_sub[0], accuracy_mul[0]], width, label="Ours", color=academic_colors[0], edgecolor='black')
plt.bar(x, [accuracy_addition[1], accuracy_sub[1], accuracy_mul[1]], width, label="Digit-wise", color=academic_colors[1], edgecolor='black')
plt.bar(x + width, [accuracy_addition[2], accuracy_sub[2], accuracy_mul[2]], width, label="Subword", color=academic_colors[2], edgecolor='black')

# Formatting
plt.xticks(x, datasets, fontsize=12, fontweight='bold')
plt.ylabel("Accuracy (%)", fontsize=14, fontweight="bold")
plt.title("Accuracy Comparison Across Methods", fontsize=16, fontweight="bold")
plt.legend(fontsize=12, frameon=True, edgecolor='black')
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='dashed', alpha=0.5)
plt.ylim(0, 105)  # Ensure labels fit neatly
plt.tight_layout()
plt.savefig("accuracy_comparison.png", dpi=300, bbox_inches="tight")

# ----- Token Usage Comparison -----
plt.figure(figsize=(10, 6))
plt.bar(x - width, [tokens[0], tokens_sub[0], tokens_mul[0]], width, label="Ours", color=academic_colors[0], edgecolor='black')
plt.bar(x, [tokens[1], tokens_sub[1], tokens_mul[1]], width, label="Digit-wise", color=academic_colors[1], edgecolor='black')
plt.bar(x + width, [tokens[2], tokens_sub[2], tokens_mul[2]], width, label="Subword", color=academic_colors[2], edgecolor='black')

# Formatting
plt.xticks(x, datasets, fontsize=12, fontweight='bold')
plt.ylabel("Tokens Used", fontsize=14, fontweight="bold")
plt.title("Token Usage Comparison", fontsize=16, fontweight="bold")
plt.legend(fontsize=12, frameon=True, edgecolor='black')
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='dashed', alpha=0.5)
plt.tight_layout()
plt.savefig("token_usage_comparison.png", dpi=300, bbox_inches="tight")

plt.show()
