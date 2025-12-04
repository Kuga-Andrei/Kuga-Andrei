########################################################
# Task A10_T3
# Developer Andrei Kuga
# Date 2025-12-1
########################################################

# A10_T3 Bubble sort (TEST TASK)
 

# Bubble sort is a well-known sorting algorithm that is renowned for its simplicity in understanding and implementation. The bubble sort algorithm organizes a list of items in either ASCending or DESCending order by repeatedly iterating through the list. During each iteration, it compares adjacent elements and swaps them if they are in the wrong order. After the first iteration, the largest (or smallest, depending on the sorting order) element will be correctly placed at the end of the list. The process then repeats for the remaining unsorted elements.

# Remaining = Items(n) − Iteration − 1

# Here, n refers to the total number of items in the list. The Big-O notation for bubble sort is O(n2), indicating that its runtime increases quadratically with the number of items. This is because the algorithm involves two nested loops. An outer loop for the iterations and an inner loop for comparisons and swaps.

# The Iteration in bubble sort corresponds to the current pass (or cycle) of the outer loop. It tracks how many times the list has been processed. The very first iteration is numbered as 0, and the last iteration occurs just before the list length.

# LastIteration = Length − 1

# The “magic number” -1 in the remaining formula is often used in implementations of bubble sort to prevent out-of-bound errors. This is because the algorithm compares each element with its next neighbor in the list. By iterating only up to n − Iteration − 1, it ensures that the last comparison in each pass stays within the valid range of the list. Additionally, this optimization reduces one unnecessary comparison on each outer cycle, improving the algorithm’s efficiency.

# On other notes, bubble sort may be easy to implement, but it is not very efficient for large inputs when compared to some other sorting algorithms.

# Visit wikipedia: Bubble sort and see the pseudocode implementation. Use it or some other source as a guide to build the sorting algorithm. Once done, ensure that the function is pure and has the interface as defined below(naming, parameters and return values). The bot will extract the function based on the A10_T3.py implementation. If you have used A10_TLib.py to store the algorithm, the bot should be able to extract it from there too.

# After the sorting algorithm is extracted successfully, it will test if the sorting algorithm works. Then it compares the extracted bubble sort algorithm into another algorithm to determine if the speed aligns with the expectations (BigO notation).

# Interface to implement. Note parameter PAsc is set by default to True. This means that the algorithm should sort everything in ascending order by default if only one argument is passed.

# def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
#     # Sort PValues by implementing bubble sort algorithm.
#     # Handle PValues list like it is a pointer to memory
#     # Sort the list inplace e.g., PValues[CurrentIndex] = PValues[NextIndex]
#     # Don't overwrite PValues identifier.
#     # Tester expects that the PValues list is modified.
#     # It doesn't catch a return value.
#     return None
# For the main program, prompt filename if there are no CLI arguments to the program. In case the len(sys.argv) is 2, then take the second argument (sys.argv[1]) and use it as a filename.

# Commands:

# # Tab 1 - Insert dataset name 'A10_D10.txt' manually
# python A10_T3.py 
# # Tab 2 - CLI Argument (sys.argv[1])
# python A10_T3.py A10_D10.txt
# # Tab 3 - CLI Argument (sys.argv[1])
# python A10_T3.py A10_D100.txt

import sys
from A10_TLib import readValues, displayValues, bubbleSortFast, bubbleSort, bubbleSortSlow

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
        # Filename = 'A10_D1000.txt'

    readValues(Filename, Values)
    # Raw list display
    print("Raw '{}' -> ".format(Filename), end='')
    displayValues(Values, Horisontally=True)
    # Sorting in ASCending order
    bubbleSort(Values)
    print("Ascending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    # Sorting in DESCending order
    bubbleSort(Values, PAsc=False) 
    print("Descending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    print('Program ending.')
    # 3. Cleanup
    Values.clear()
    return None

if __name__ == "__main__":
    main()