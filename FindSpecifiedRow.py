# Check whether a NumPy array contains a specified row.
import numpy as np

original_array = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

specified_row = np.array([5, 5, 6])

for row in original_array:
    if(np.array_equal(row, specified_row)):
        row_exists=True
        break
    else:
        row=False
if row_exists:
    print("The specified row exists in the array.")
else:
    print("The specified row does not exist in the array.")
