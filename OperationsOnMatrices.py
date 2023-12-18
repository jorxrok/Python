import numpy as np

# Create two matrices
matrix_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix_b = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Add two matrices
sum_matrix = np.add(matrix_a, matrix_b)

# Multiply two matrices
product_matrix = np.dot(matrix_a, matrix_b)

# Display the matrices and results
print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nSum of Matrix A and Matrix B:")
print(sum_matrix)

print("\nProduct of Matrix A and Matrix B:")
print(product_matrix)
