########################################################
# Task A10_T2
# Developer Andrei Kuga
# Date 2025-11-30
########################################################

########################
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston, kun ajaa ohjelman toisesta kansiosta. 
ROOT_DIR = Path(__file__).parent
########################

# A10_T2 Aggregate data
# Create a program that can analyse integers in a text file. Filter empty rows and strip the newline characters so that each row can be converted into an integer datatype.

# Analysis:

# Calculate the sum of the numbers
# Calculate the product of the numbers

import sys # for possible exit on errors

def readValues(PFilename: str, PValues: list[int]) -> None:
    filepath = ROOT_DIR / PFilename
    try:
        with open(filepath, 'r') as f:
            for i in f:
                if i == '\n':
                    continue
                i.strip('\n')
                i = int(i)
                PValues.append(i)
    except IOError:
        print('Couldn\'t open file "{}".'.format(PFilename))
        print('Exiting program.')
        sys.exit(-1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    Sum = sum(PValues)
    return Sum

def productOfValues(PValues: list[int]) -> int:
    Product = 1
    for i in PValues:
        Product *= i
    return Product

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    # 2. Operate
    print("Program starting.")
    # 2.1 ask filename
    Filename = input('Insert filename: ')
    # 2.2 read values
    readValues(Filename, Values)
    # 2.3 calculate sum of values
    Sum = sumOfValues(Values)
    # 2.4 calculate product of values
    Product = productOfValues(Values)
    # 2.5 display results
    print('# --- Sum of numbers --- #')
    print(Sum)
    print('# --- Sum of numbers --- #')
    print('# --- Product of numbers --- #')
    print(Product)
    print('# --- Product of numbers --- #')
    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()