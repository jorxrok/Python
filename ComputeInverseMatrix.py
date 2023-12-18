# Create a Numpy program to compute the inverse of a matrix
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)

print("Original Matrix:\n", matrix)
print("Inverse Matrix:\n", inverse_matrix)
