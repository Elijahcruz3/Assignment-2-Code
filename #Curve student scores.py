#Curve student scores

# TODO: Import NumPy
import numpy as np

# TODO: Load student scores from file_name into a NumPy array
file_name = 'scores_test1.txt'  # Specify your filename here
with open(file_name, 'r') as file:
    scores = np.array(list(map(int, file.read().split())))

# TODO: Calculate the median and average of student scores
median_score = np.median(scores)
average_score = np.mean(scores)

# TODO: Curve student scores
curved_scores = scores + (100 - np.max(scores))

# TODO: Output the median, average, and curved scores
print(f"Median = {median_score:.2f}")
print(f"Average = {average_score:.2f}")
print(f"Curved scores = {curved_scores}")