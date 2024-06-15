"""
Question 1:
 Create a function create_custom_identity(size, value, index) that takes three arguments:

size: Size of the square identity matrix (e.g., 4).

value: The value to insert at the specified index (e.g., 10).

index: A tuple representing the index (i, j) for the custom value.

The function should return a NumPy array representing the identity matrix with the specified value inserted
at the given index.
"""

import numpy as np


def create_custom_identity(size, value, index):
    # Create a matrix of zeros with the specified size
    identity_matrix = np.identity(size)

    # Set the diagonal elements to ones
    for i in range(size):
        identity_matrix[i, i] = 1

    # Insert the custom value at the specified index
    identity_matrix[index[0], index[1]] = value
    return identity_matrix


matrix = create_custom_identity(4, 10, (1, 2))
print(matrix)


