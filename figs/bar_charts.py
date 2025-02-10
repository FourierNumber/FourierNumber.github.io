import matplotlib.pyplot as plt
import numpy as np

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
academic_colors = ["#D62728", "#ADD8E6", "#808080"]  # Red for "Ours", White Blue, Grey

# Redefining x-axis to group by dataset instead of method
datasets = ["Addition", "Subtraction", "Multiplication"]
x = np.arange(len(datasets))  # Label locations
width = 0.2  # Bar width

# Plotting Training Time Comparison
plt.figure(figsize=(10, 5))
plt.bar(x - width, [train_times[0], train_times_sub[0], train_times_mul[0]], width, label="Ours", color=academic_colors[0])
plt.bar(x, [train_times[1], train_times_sub[1], train_times_mul[1]], width, label="Digit-wise", color=academic_colors[1])
plt.bar(x + width, [train_times[2], train_times_sub[2], train_times_mul[2]], width, label="Subword", color=academic_colors[2])
plt.xticks(x, datasets, fontsize=12)
plt.ylabel("Time (seconds)", fontsize=12)
plt.title("Training and Test Time for One Epoch Comparison", fontsize=14)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("training_time_comparison.png")

# Plotting Accuracy Comparison
plt.figure(figsize=(10, 5))
plt.bar(x - width, [accuracy_addition[0], accuracy_sub[0], accuracy_mul[0]], width, label="Ours", color=academic_colors[0])
plt.bar(x, [accuracy_addition[1], accuracy_sub[1], accuracy_mul[1]], width, label="Digit-wise", color=academic_colors[1])
plt.bar(x + width, [accuracy_addition[2], accuracy_sub[2], accuracy_mul[2]], width, label="Subword", color=academic_colors[2])
plt.xticks(x, datasets, fontsize=12)
plt.ylabel("Accuracy (%)", fontsize=12)
plt.title("Accuracy Comparison", fontsize=14)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("accuracy_comparison.png")

# Plotting Token Usage Comparison
plt.figure(figsize=(10, 5))
plt.bar(x - width, [tokens[0], tokens_sub[0], tokens_mul[0]], width, label="Ours", color=academic_colors[0])
plt.bar(x, [tokens[1], tokens_sub[1], tokens_mul[1]], width, label="Digit-wise", color=academic_colors[1])
plt.bar(x + width, [tokens[2], tokens_sub[2], tokens_mul[2]], width, label="Subword", color=academic_colors[2])
plt.xticks(x, datasets, fontsize=12)
plt.ylabel("Tokens Used", fontsize=12)
plt.title("Token Usage Comparison", fontsize=14)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("token_usage_comparison.png")
