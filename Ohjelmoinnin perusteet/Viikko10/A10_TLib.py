"""
This program file acts as a program library containing different
functionalities for the other programs to consume.
"""
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
        sys.exit(1) # 1 - virhetilanne
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

def quickSort(PArr: list[int], PLow: int = None, PHigh: int = None, PAsc: bool = True) -> None:
    if PLow == None: PLow = 0
    if PHigh == None: PHigh = len(PArr) - 1
    if PLow < PHigh:
        # Partition the array and get the pivot index
        PivotIndex = partition(PArr, PLow, PHigh, PAsc)
        # Recursively apply quick sort to the left and right subarrays
        quickSort(PArr, PLow, PivotIndex - 1, PAsc)
        quickSort(PArr, PivotIndex + 1, PHigh, PAsc)
    return None

def plotNumbers(PNumbers: list[int], PTitle: str, Save=True) -> None:
    xAxis = [(i + 1) for i in range(len(PNumbers))]
    plt.plot(xAxis, PNumbers)
    plt.ylabel("Value")
    plt.title(PTitle)
    if Save:
        plt.savefig(PTitle + '.png')
    else:
        plt.show()
    plt.clf() # Clear current figure
    return None

def displayValues(Values: list[str|int|float], Horisontally=False) -> None:
    for i, Value in enumerate(Values):
        if Horisontally:
            if i == len(Values) - 1:
                print(Value)
            else:
                Part = str(Value) + ", "
                print(Part, end='')
        else:
            print(Value)
    return None

#################################################################
# Omat funktiot
##############################################
# Bubblle sort funktiot, kolme eri toteutusta Slow on hitain, Fast on nopein ja ilman lisätekstiä niiden välillä
##############################################

def bubbleSortSlow(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    # Iteration for testing
    # iteration = 0
    for i in range(n):
        for j in range(n - i - 1):
            # iteration += 1
            if (PValues[j] > PValues[j+1] and PAsc) or (PValues[j] < PValues[j+1] and not PAsc):
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]
    # print('Iterations:', iteration)

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    swap = True
    # Iteration for testing
    # iteration = 0
    while swap:
        swap = False
        for i in range(n-1):
            # iteration += 1
            if (PValues[i] > PValues[i+1] and PAsc) or (PValues[i] < PValues[i+1] and not PAsc):
                PValues[i], PValues[i+1] = PValues[i+1], PValues[i]
                swap = True
        n = n-1
    # print('Iterations:', iteration)

def bubbleSortFast(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    # Iteration for testing
    # iteration = 0
    while n > 1:
        newn = 0
        for i in range(1,n):
            # iteration += 1
            if (PValues[i-1] > PValues[i] and PAsc) or (PValues[i-1] < PValues[i] and not PAsc):
                PValues[i-1], PValues[i] = PValues[i], PValues[i-1]
                newn = i
        n = newn
    # print('Iterations:', iteration)
    return None

##############################################
# Merge Sort funktiot
##############################################
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
    return None
#################################################################