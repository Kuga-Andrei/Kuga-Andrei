########################################################
# Task A10_T1
# Developer Andrei Kuga
# Date 2025-11-29
########################################################

########################
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston, kun ajaa ohjelman toisesta kansiosta. 
ROOT_DIR = Path(__file__).parent
########################

# A10_T1 Read and display data
# First download the datasets above. Then create a program which prompts user to insert a filename and then displays the file content in two different ways:

# Vertically - Each value on its own row.
# Horizontally - Values on the same row, separated by comma and space “, ”.
# While reading the file rows, strip the newline characters and ignore empty rows.

def readFile(PFilename: str, PData: list[int]) -> None:
    filepath = ROOT_DIR / PFilename
    with open(filepath, 'r') as f:
        for i in f:
            if i == '\n':
                continue
            i.strip('\n')
            i = int(i)
            PData.append(i)

def displayData(PData: list[int], POrient: str) -> None:
    '''Displays Data vertically or horizontally. Second argumment "Vertically" or "Horizontally"'''
    print('# --- {} --- #'.format(POrient))
    if POrient == 'Vertically':
        for i in PData:
            print(i)
        print('# --- {} --- #'.format(POrient))
    elif POrient == 'Horizontally':
        for i in PData:
            if i is PData[-1]:
                print(i, end='\n')
            else:
                print(i, end=', ')
        print('# --- {} --- #'.format(POrient))


def main():
    print('Program starting.')
    Data: list[int] = []
    Filename = input('Insert filename: ')
    try:
        readFile(Filename, Data)
        displayData(Data, 'Vertically')
        displayData(Data, 'Horizontally')
    except IOError:
        print('Couldn\'t open file "{}".'.format(Filename))
    Data.clear()
    print('Program ending.')

if __name__ == "__main__":
    main()