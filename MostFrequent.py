# Find the most frequent value in a NumPy array:
import numpy as np

arr = np.array([1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 5])

most_frequent_value = np.bincount(arr).argmax()

print("Most frequent value:", most_frequent_value)
