# Flatten a 2D NumPy array into a 1D array:
import numpy as np

matrix_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

flattened_array = matrix_2d.flatten()

print("Flattened 1D array:")
print(flattened_array)
    