########################################################
# Task A10_T6
# Developer Andrei Kuga
# Date 2025-12-2
########################################################

import copy
import time
from typing import Callable
import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    PValues.clear()
    try:
        Filehandle = open(PFilename, 'r', encoding="UTF-8")
        while True:
            Line = Filehandle.readline() # Read line and move stream position to next line
            if (len(Line) == 0): # File ends
                break
            elif (Line == '\n'): # Empty line
                continue
            else:
                Row = Line.rstrip('\n') # This right strip removes newline from the right side 
                Value = int(Row) # Convert string to integer
                PValues.append(Value)
        Filehandle.close() # Vapautetaan varatut resurssit takaisin järjestelmälle
    except Exception:
        print("Couldn't read file '{}'.".format(PFilename))
        return None # 1 - virhetilanne
    return None

def writeResults(PFilename: str, PFilenameOrigin: str, PResults: list[str], PResultsNames: list[str]) -> None:
    with open(PFilename, 'w', encoding='UTF-8') as f:
        f.write("Measured speeds for dataset '{}':\n".format(PFilenameOrigin))
        for i in range(len(PResults)):
            f.write(' - {} {} ns\n'.format(PResultsNames[i], PResults[i]))
    return None

def partition(PArr: list[int], PLow: int, PHigh: int, PAsc: bool) -> int:
    # Choose the last element as pivot
    Pivot = PArr[PHigh]
    i = PLow - 1  # Pointer for the smaller element
    for j in range(PLow, PHigh):
        # If current element is smaller than or equal to the pivot
        if (PArr[j] <= Pivot and PAsc) or (PArr[j] >= Pivot and not PAsc):
            i += 1
            # Swap the elements
            TempElem = PArr[i]
            PArr[i] = PArr[j]
            PArr[j] = TempElem
    # Swap the pivot element with the element at i + 1
    TempElem = PArr[i + 1]
    PArr[i + 1] = PArr[PHigh]
    PArr[PHigh] = TempElem
    # Set pivot index
    PivotIndex = i + 1
    return PivotIndex

def quickSort(PNums: list[int], PLow: int = None, PHigh: int = None, PAsc: bool = True) -> list[int]:
    if PLow == None: PLow = 0
    if PHigh == None: PHigh = len(PNums) - 1
    if PLow < PHigh:
        # Partition the array and get the pivot index
        PivotIndex = partition(PNums, PLow, PHigh, PAsc)
        # Recursively apply quick sort to the left and right subarrays
        quickSort(PNums, PLow, PivotIndex - 1, PAsc)
        quickSort(PNums, PivotIndex + 1, PHigh, PAsc)
    return PNums

def bubbleSortBasic(PValues: list[int]) -> list[int]:
    n = len(PValues)
    for i in range(n):
        for j in range(n - i - 1):
            if PValues[j] > PValues[j+1]:
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]
    return PValues

def bubbleSort(PValues: list[int]) -> list[int]:
    n = len(PValues)
    swap = True
    while swap:
        swap = False
        for i in range(n-1):
            if PValues[i] > PValues[i+1]:
                PValues[i], PValues[i+1] = PValues[i+1], PValues[i]
                swap = True
        n = n-1
    return PValues

def bubbleSortLess(PValues: list[int]) -> list[int]:
    n = len(PValues)
    while n > 1:
        newn = 0
        for i in range(1,n):
            if PValues[i-1] > PValues[i]:
                PValues[i-1], PValues[i] = PValues[i], PValues[i-1]
                newn = i
        n = newn
    return PValues

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    PMerge.clear()
    while (len(PLeft) and len(PRight)) >= 1:
        if (PLeft[0] <= PRight[0] and PAsc) or (PLeft[0] >= PRight[0] and not PAsc):
            PMerge.append(PLeft[0])
            PLeft.pop(0)
        else:
            PMerge.append(PRight[0])
            PRight.pop(0)
    PMerge += PRight
    PMerge += PLeft
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    left = []
    right = []
    if len(PValues) > 1:
        middle = len(PValues) // 2
        left = PValues[0:middle]
        mergeSort(left, PAsc)
        right = PValues[middle:]
        mergeSort(right, PAsc)
        merge(left, right, PValues, PAsc)
    return PValues

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr) # param is function
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime

def showOptions() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        choice = int(choice)
        return choice
    else:
        return -1

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    Results: list[str] = []
    Filename = False
    # 2. Operate
    print("Program starting.")
    try:
        while True:
            showOptions()
            choice = askChoice()
            match choice:
                case 1:
                    Filename = input('Insert dataset filename: ')

                    ###################################
                    # # For quick input
                    # quick = int(input('FileIndex: '))
                    # FilenameList = ['A10_D10.txt', 'A10_D100.txt', 'A10_D1000.txt']
                    # Filename = FilenameList[quick]
                    ###################################

                    readValues(Filename, Values)
                    print()
                case 2:
                    if Filename:
                        # pass algorithm into the measureSortingTime function # import copy
                        BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
                        BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
                        QuickSortTimeNs = measureSortingTime(quickSort, copy.deepcopy(Values))
                        BubbleSortBasicTimeNs = measureSortingTime(bubbleSortBasic, copy.deepcopy(Values))
                        BubbleSortLessTimeNs = measureSortingTime(bubbleSortLess, copy.deepcopy(Values))
                        MergeSortNs = measureSortingTime(mergeSort, copy.deepcopy(Values)) 
                        Results.clear()
                        Results.append(BuiltinSortedTimeNs) 
                        Results.append(BubbleSortTimeNs) 
                        Results.append(QuickSortTimeNs)
                        Results.append(BubbleSortBasicTimeNs) 
                        Results.append(BubbleSortLessTimeNs) 
                        Results.append(MergeSortNs)
                        ResultsNames = ['Built-in sorted', 'Buble sort', 'Quick sort', 'Basic buble sort', 'Buble sort with less iterations', 'Merge sort']
                        print("Measured speeds for dataset '{}':".format(Filename))
                        for i in range(len(Results)):
                            print(' - {} {} ns'.format(ResultsNames[i], Results[i]))
                        print()
                    else:
                        print('No loaded dataset\n')
                case 3:
                    resultsFilename = input('Insert results filename: ')

                    ###################################
                    # For quick input
                    # resultsquick = quick
                    # resultsFilenameList = ['A10_D10_Results.txt', 'A10_D100_Results.txt', 'A10_D1000_Results.txt']
                    # resultsFilename = resultsFilenameList[resultsquick]
                    ###################################

                    writeResults(resultsFilename, Filename, Results, ResultsNames)
                    print()
                case 0:
                    print('Exiting program.\n')
                    break 
                case _:
                    print("Unknown option.\n")
    except KeyboardInterrupt:
        print('Closing program')
        sys.exit(1)

    # 3. Cleanup
    Values.clear()
    Results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()


# A10_T6 Sorting algorithm speed tests
# Create a menu-driven program which is able to measure nano seconds spent on sorting. In this exercise, use datasets A10_D10.txt, A10_D100.txt and A10_1000.txt.

# Implement and/or use three sorting algorithm:
# Built-in sorted
# Bubble sort
# Quick sort
# Build menu-driven program with 4 options
# 1 - Read dataset values
# 2 - Measure speeds
# 3 - Save results
# 0 - Exit
# Measure the sorting time on ascending order using the “time.perf_counter_ns()” function. Sorting time can be calculated by subtracting starting time from the stopping time.

# Functions can also be passed as an argument to other functions. Just omit the parentheses () when doing so. The datatype is Callable which can be imported from the typing library.

# Also copy the original dataset using for example copy.deepcopy function so that the next sorting algorithm doesn’t receive already sorted array. Import the copy module first.

# See code examples below:

# import copy
# import time
# from typing import Callable

# def readValues(PValues: list[int|float]) -> None:
#     # clear values list to ensure no duplicate data (reading twice)
#     # open filehandle
#     # read line-by-line
#     #   # parse value(int) from line(str + '\n')
#     #   # append value into the values list
#     # close filehandle
#     return None

# def quickSort(PNums: list[int]) -> list[int]:
#     # https://en.wikipedia.org/wiki/Bubble_sort
#     return PNums

# def bubbleSort(PNums: list[int]) -> list[int]:
#     # https://en.wikipedia.org/wiki/Quicksort
#     return PNums

# def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
#     StartTime = time.perf_counter_ns()
#     PSortingAlgorithm(PArr) # param is function
#     EndTime = time.perf_counter_ns()
#     ElapsedTime = EndTime - StartTime
#     return ElapsedTime

# def main() -> None:
#     # 1. Initialize
#     Values: list[int] = []
#     Results: list[str] = []
#     # 2. Operate
#     print("Program starting.")
#     readValues(Values)
#     # ...
#         # pass algorithm into the measureSortingTime function # import copy
#         BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
#         BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
#         # check if 
#     # 3. Cleanup
#     Values.clear()
#     Results.clear()
#     print("Program ending.")
#     return None
# Example program run:

# Note! the speed results may vary. Measuring speeds using “A10_D100.txt” or “A10_D1000.txt”, the built-in sorted should be the quickest, followed by quick sort and slowest sorting algorithm should be bubble sort..