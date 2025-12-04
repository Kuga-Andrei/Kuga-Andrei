########################################################
# Task A10_T4
# Developer Andrei Kuga
# Date 2025-12-2
########################################################

import sys
from A10_TLib import readValues, displayValues, mergeSort

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    Filename = ""
    # 2. Operate
    print('Program starting.')
    if (len(sys.argv) == 2):
        Filename = sys.argv[1]
        print("The filename '{}' was passed via CLI.".format(Filename))
    else:
        Filename = input('Insert filename: ')

        # For testing
        # Filename = 'A10_D100.txt'

    readValues(Filename, Values)
    # Raw list display
    print("Raw '{}' -> ".format(Filename), end='')
    displayValues(Values, Horisontally=True)
    # Sorting in ASCending order
    mergeSort(Values)
    print("Ascending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    # Sorting in DESCending order
    mergeSort(Values, PAsc=False) 
    print("Descending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    print('Program ending.')
    # 3. Cleanup
    Values.clear()
    return None

if __name__ == "__main__":
    main()

# A10_T4 Merge sort (TEST TASK)

# Merge sort is a divine-and-conquer sorting algorithm that splits an array into smaller subarrays, recursively sorts them, and then merges them back to gether in sorted order. It is very efficient sorting algorithm in terms of time and space complexity. It is also stable. One down side is that it is not sorting in-place, which means that it requires additional memory for merging.

# The merge sort pseudocode example below describes important aspects on how to implement it.

# function merge(left, right):
#     result = empty array
#     while left and right are not empty:
#         if left[0] ≤ right[0]:  # Change to ≥ for descending order
#             append left[0] to result
#             remove left[0] from left
#         else:
#             append right[0] to result
#             remove right[0] from right
#     append remaining elements of left and right to result
#     return result

# function mergeSort(array):
#     if size of array ≤ 1:
#         return array
#     mid = size of array // 2
#     left = mergeSort(array[0:mid])
#     right = mergeSort(array[mid:])
#     return merge(left, right)
# Expected interface for the algorithm:

# def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
#     return None

# def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
#     # Sort PValues.
#     # PAsc: in ascending order by default. False will sort in descending order.
#     return None