# Calculate the sum of all columns in a 2D NumPy array:
import numpy as np

matrix_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

column_sums = np.sum(matrix_2d, axis=0)

print("Sum of each column:")
print(column_sums)
