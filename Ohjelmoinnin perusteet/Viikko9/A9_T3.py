########################################################
# Task A9_T2
# Developer Andrei Kuga
# Date 2025-11-25
########################################################

# A9_T3 File exists
# Write a small Python program which read a text file. If the file doesn’t exist, the program must print error message to the user and the program must exit with code 1. Otherwise print the file content and continue program run normally.

# Test file
# A9_T3_D1.txt
# Example program runs:

# Tab 1 Tab 2 Tab 3
# Program starting.
# Insert filename: A9_T3_D1.txt
# ## A9_T3_D1.txt ##
# File
# exists
# ## A9_T3_D1.txt ##
# Program ending.

# Example solution contains 30 lines of code.

import sys
########################
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston, kun ajaa ohjelman toisesta kansiosta. 
ROOT_DIR = Path(__file__).parent
########################

def readFile(fileName: str, content: list) -> list:
    content = []
    fileLocation = ROOT_DIR / fileName #Etsii tiedoston samasta kansiosta kuin ohjelma
    try:
        with open(fileLocation, 'r') as f:
            for i in f:
                line = i.strip()
                content.append(line)
        return content

    except IOError:
        print('Couldn\'t read file "{}".\n'.format(fileName))
        sys.exit(1)

def showContent(fileName: str, content: list):
    print('## {} ##'.format(fileName))
    for i in content:
        print(i)
    print('## {} ##'.format(fileName))
    
def main():
    content = []
    print('Program starting.')
    fileName = input('Insert filename: ')
    content = readFile(fileName, content)
    showContent(fileName, content)
    print('Program ending.')

if __name__ == "__main__":
    main()