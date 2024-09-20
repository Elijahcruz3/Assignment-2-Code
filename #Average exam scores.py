#Average exam scores

# TODO: Import NumPy
import numpy as np

# TODO: Read two sets of exam scores of five students from user input
#       and store the scores into two NumPy arrays 
exam1 = np.array([85, 80, 30, 82, 92])  # First set of scores
exam2 = np.array([98, 86, 76, 20, 73])  # Second set of scores

# TODO: Compute the average scores for each of the five students
average_scores = (exam1 + exam2) / 2

# TODO: Output "Average scores: " followed by the NumPy array of the average scores
print(f"Average scores: {average_scores}")

# TODO: Count the number of average scores that are >= 80
count_above_80 = np.sum(average_scores >= 80)

# TODO: Output "Number of students who received 80 and above: " followed by the count
print(f"Number of students who received 80 and above: {count_above_80}")