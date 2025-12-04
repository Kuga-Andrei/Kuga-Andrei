########################################################
# Task A10_T7
# Developer Andrei Kuga
# Date 2025-12-4
########################################################
"""
Ready minefield below
[
  [9, 3, 9, 3, 1, 0], # row 1
  [1, 3, 9, 9, 1, 0], # row 2
  [1, 2, 3, 2, 1, 0], # row 3
  [1, 9, 1, 0, 1, 1], # row 4
  [2, 3, 2, 1, 1, 9], # row 5
  [9, 2, 9, 1, 1, 1], # row 6
  [1, 2, 1, 1, 0, 0]  # row 7
]

Numbers:
0 - zero nearby mines
1 - one nearby mine
2 - two nearby mines
3 - three nearby mines
4 - four nearby mines
5 - five nearby mines
6 - six nearby mines
7 - seven nearby mines
8 - eight nearby mines
9 - mine
"""
import random
import sys
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
    """
    The "PMineField" is pre-initialized 2d matrix with zeros.
    [
        [0, 0, 0, 0, 0, 0], # row 1
        [0, 0, 0, 0, 0, 0], # row 2
        [0, 0, 0, 0, 0, 0], # row 3
        [0, 0, 0, 0, 0, 0], # row 4
        [0, 0, 0, 0, 0, 0], # row 5
        [0, 0, 0, 0, 0, 0], # row 6
        [0, 0, 0, 0, 0, 0]  # row 7
    ]
    Randomly places mines to the PMineField.
    [
        [9, 0, 9, 0, 0, 0], # row 1
        [0, 0, 9, 9, 0, 0], # row 2
        [0, 0, 0, 0, 0, 0], # row 3
        [0, 9, 0, 0, 0, 0], # row 4
        [0, 0, 0, 0, 0, 9], # row 5
        [9, 0, 9, 0, 0, 0], # row 6
        [0, 0, 0, 0, 0, 0]  # row 7
    ]
    """
    layedMines = 0
    while layedMines < PMines:
        ranRow = random.randint(0, len(PMineField) - 1)
        ranCol = random.randint(0, len(PMineField[0]) - 1)
        if PMineField[ranRow][ranCol] == 0: #place mine only if empty
            PMineField[ranRow][ranCol] = 9
            layedMines += 1
    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:
    """
    Expects 2d-matrix with mines layed:
    [
        [9, 0, 9, 0, 0, 0], # row 1
        [0, 0, 9, 9, 0, 0], # row 2
        [0, 0, 0, 0, 0, 0], # row 3
        [0, 9, 0, 0, 0, 0], # row 4
        [0, 0, 0, 0, 0, 9], # row 5
        [9, 0, 9, 0, 0, 0], # row 6
        [0, 0, 0, 0, 0, 0]  # row 7
    ]

    Calculates nearby mines:
    [
        [9, 3, 9, 3, 1, 0], # row 1
        [1, 3, 9, 9, 1, 0], # row 2
        [1, 2, 3, 2, 1, 0], # row 3
        [1, 9, 1, 0, 1, 1], # row 4
        [2, 3, 2, 1, 1, 9], # row 5
        [9, 2, 9, 1, 1, 1], # row 6
        [1, 2, 1, 1, 0, 0]  # row 7
    ]
    """
    nearby = 0
    pos = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for row in range(len(PMineField)):
        for col in range(len(PMineField[row])):
            nearby = 0
            if PMineField[row][col] == 9:
                continue
            elif  row == 0:
                if col == 0:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if i[1] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                elif col == len(PMineField[row])-1:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if i[1] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                else:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
            elif  row == len(PMineField)-1:
                if col == 0:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if i[1] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                elif col == len(PMineField[row])-1:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if i[1] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                else:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
            else:
                if col == 0:
                    for i in pos:
                        if i[1] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                elif col == len(PMineField[row])-1:
                    for i in pos:
                        if i[1] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                else:
                    for i in pos:
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
    return None

def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    """
    Takes empty "PMineField" list and amount of rows, columns and mines as parameters.
    """
    # Clear minefield
    PMineField.clear()
    # Generate Minefield with only zeros
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)
    # Laying mines
    layMines(PMineField, PMines)
    # Calculating nearbys
    calculateNearbys(PMineField)
    return None

def showOptions() -> None:
    print('Options:')
    print('1 - Generate minesweeper board')
    print('2 - Show generated board')
    print('3 - Save generated board')
    print('0 - Exit')

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        choice = int(choice)
        return choice
    else:
        return -1

def writeResults(PFilename: str, PMineField: list[list[int]]) -> None:
    with open(PFilename, 'w', encoding='UTF-8') as f:
        for row in PMineField:
            f.write(','.join(str(i) for i in row)+'\n')
    return None

def main() -> None:
    # Initialize
    MineField = []
    try:
        while True:
            showOptions()
            choice = askChoice()
            match choice:
                case 1:
                    Rows = input('Insert rows: ')
                    Cols = input('Insert columns: ')
                    Mines = input('Insert mines: ')
                    # Rows = '6' #Test
                    # Cols = '6' #Test
                    # Mines = '8' #Test
                    try:
                        Rows = int(Rows)
                        Cols = int(Cols)
                        Mines = int(Mines)
                        generateMinefield(MineField, Rows, Cols, Mines)
                    except ValueError:
                        print('Operation failed.')
                        print('All inputs must be numbers.')
                    print()

                case 2:
                    for i in MineField:
                        print(i)
                    print()

                case 3:
                    Filename = input('Insert filename: ')
                    # Filename = 'A10_T7_Test.txt'
                    writeResults(Filename, MineField)
                    print()
                case 0:
                    print('Exiting program.\n')
                    break 
                case _:
                    print("Unknown option.\n")
    except KeyboardInterrupt:
        print('Closing program')
        sys.exit(1)

    # Cleanup
    MineField.clear()
    print("Program ending.")
    return None

main()


# A10_T7 Minesweeper field
# Minesweeper is a classic puzzle game where player uncovers tiles on a grid while avoiding hidden mines. The goal is to clear the board by revealing all non-mine tiles or flagging all mines without triggering one.



# The entire Minesweeper game can be implemented in approximately 500 lines of Python or JavaScript code, depending on the approach and complexity. This exercise aims to guide you on this journey by introducing the first step of game development, which is the board creation (~150 lines of code).

# Design three Python functions to create a minefield for the Minesweeper game:

# You can add additional helper functions if needed, but the specified functions must remain in place with the provided interface and adhere to the described behaviour in the documentation. Functions layMines, calculateNearbys and generateMinefield will be extracted from the code and tested to ensure proper functionality and validation.

# Note! in this exercise, avoid using multiple program files. Create one python file A10_T7.py.