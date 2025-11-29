########################################################
# Task A9_T7
# Developer Andrei Kuga
# Date 2025-11-29
########################################################

########################
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston, kun ajaa ohjelman toisesta kansiosta. 
ROOT_DIR = Path(__file__).parent
########################

# A9_T7 CLI Copy tool with error handling
# Create a CLI tool for copying text files (similar to A6_T3). This time around, parse CLI arguments and write error handling to the program.

# A9_T7 Datasets
# A9_T7_D1.txt
# A9_T7_D2.txt
# A9_T7_D3.txt
# CLI Arguments is a new topic, and we will dive into them later in the course (extras). Python provides access to the CLI arguments via sys.argv, which is a list of strings.

# Example below illustrates how to access all CLI arguments:

# import sys

# def main() -> None:
#     print("Program starting.")
#     for i in range(len(sys.argv)):
#         print("arg_{}: {}".format(i, sys.argv[i]))
#     print("Program ending.")
#     return None

# main()
# Provide the arguments via CLI for example:

# user@host:~/projects/ohj
# $ python A9_T7.py src_file.txt dst_file.txt
# Program starting.
# arg_0: A9_T7.py
# arg_1: src_file.txt
# arg_2: dst_file.txt
# Program ending.
# user@host:~/projects/ohj
# $ 
# To check if a file exists, one could use os.path.exists-function.

# import os

# Filename = input("Insert filename: ")
# if (os.path.exists(Filename)):
#     print('File "{}" exists.'.format(Filename))
# else:
#     print('File "{}" doesn\'t exists.'.format(Filename))
# In this exercise, write the program to handle following cases(see order):

# Argument amount must be 3 (python_filename, src_file, dst_file) - if there are more or less arguments, inform user that there is invalid amount of arguments followed by the synopsis (CLI tool usage).
# Test if destination file exists (prompt user to overwrite)
# Try to open and copy files. If the operation fails, inform the user and exit program with exit code -1. Possible failure could occur if the source file doesn’t exist.
import sys
import os

def showHelp() -> None:
    # ...
    pass

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    Proceed = False # One-way flag
    print('Copying file "{}" to "{}".'.format(PSrcFile,PDstFile))
    if (os.path.exists(PDstFile)):
        print('Destination file "{}" already exists.'.format(PDstFile))
        while True:
            overwrite = input('Do you want to overwrite it? (y/n): ')
            if overwrite == 'y':
                Proceed = True
                break
            elif overwrite == 'n':
                break
            else:
                print('Unknown option.')
    else:
        Proceed = True
    
    if Proceed:
        try:
            with open(PSrcFile, 'r') as Sf, open(PDstFile, 'w') as Df:
                Df.write(Sf.read())
        except IOError:
            print("Couldn't copy \"{}\" to \"{}\".".format(PSrcFile,PDstFile))
            print('Exiting program.')
            sys.exit(-1)

def main() -> None:
    print("Program starting.")
    if (len(sys.argv) == 3):
        SrcFile = sys.argv[1]
        DstFile = sys.argv[2]
        print('Source file "{}"'.format(SrcFile))
        print('Destination file "{}"'.format(DstFile))
        copyFile(SrcFile, DstFile)
    else:
        print('Invalid amount of argumets.')
        print('[USAGE] python A9_T7.py src_file dst_file')
    print('Program ending.')

if __name__ == "__main__":
    main()