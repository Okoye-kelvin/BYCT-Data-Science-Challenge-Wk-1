"""
Question 3:
Write a function safe_add(arr1, arr2) that adds two NumPy arrays and handles potential broadcasting issues gracefully.
The function should raise a specific error message if the shapes of the arrays are incompatible for addition.
"""

import numpy as np

# Define a function to safely add two NumPy arrays
def safe_add(arr1, arr2):
    # Check if the arrays have the same shape
    if arr1.shape != arr2.shape:
        # If not, raise a ValueError with a message
        raise ValueError("Arrays are incompatible for addition")
    # If the arrays have the same shape, return their sum
    return arr1 + arr2


# First test: Add two 3x3 arrays
print("First Test: \n")
arr1 = np.random.randint(1, 10, size=(3, 3))  # Generate a random 3x3 array
arr2 = np.random.randint(2, 11, size=(3, 3))  # Generate another random 3x3 array
print(safe_add(arr1, arr2), "\n")  # Print the sum of the two arrays

# Second test: Try to add a 1D array and a 2D array
print("Second Test: ")
arr1 = np.array([1, 2, 3])  # Define a 1D array
arr2 = np.array([[6, 3, 5], [2, 3, 4]])  # Define a 2D array
try:
    print(safe_add(arr1, arr2), )  # Try to add the two arrays
except ValueError as e:
    print(e)  # If a ValueError is raised, print the error message
