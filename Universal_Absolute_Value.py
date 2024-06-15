"""
Question 5:
Define a function absolute_all(arr) that takes a NumPy array and
returns a new array with all elements converted to their absolute values.
"""
import numpy as np


# Define a function to calculate the absolute values of all elements in a NumPy array
def absolute_all(arr):
    return arr


# Generate a random 3x3 array with values between -2 and 7
arr = np.random.randint(-2, 8, size=(3, 3))

# Print the original array
print("Array: \n", arr, "\n")

# Calculate the absolute values of all elements in the array
absolute_result = np.abs(arr)

# Print the result
print("Absolute Result: \n", absolute_result)
