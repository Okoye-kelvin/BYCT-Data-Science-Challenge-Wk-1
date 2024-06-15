"""
Question 2:
 Write a function check_same_elements(arr1, arr2) that takes two NumPy arrays and returns True if both arrays contain
    the same elements regardless of their order, False otherwise.
 (Hint: Explore sorting and set comparisons).
"""

import numpy as np


def check_same_element():
    # creating a random 3x3 array
    arr1 = np.random.randint(1, 5, size=(3, 3))
    print("First Array: \n\n", arr1)

    arr2 = np.random.randint(4, 12, size=(3, 3))
    print("\nSecond Array: \n\n", arr2)

    # Flatten the arrays
    array1_flat = arr1.flatten()
    array2_flat = arr2.flatten()

    # converting the 1-D array into a set
    set1 = set(array1_flat)
    set2 = set(array2_flat)

    # return false if same element not in the both array, otherwise true
    return not set1.isdisjoint(set2)


print("\n", "Result: ", check_same_element())
