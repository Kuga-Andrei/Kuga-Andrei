########################################################
# Task A9_T2
# Developer Andrei Kuga
# Date 2025-11-25
########################################################

# A9_T2 Exit codes
# Prompt the user to insert exit code. Exit the program with using sys.exit and the user defined exit code. Remember to convert the value into an integer. sys.exit expects value between 0-255.

# sys.exit usage:

# import sys

# sys.exit(0) # Success exit code
# sys.exit(1) # Error exit code
# Example program runs:

# Tab 1 Tab 2 Tab 3
# Program starting.
# Insert exit code(0-255): 0
# Clean exit

import sys

def main():
    print('Program starting.')
    exitCode = input('Insert exit code(0-255): ')
    if exitCode == '0':
        print('Clean exit')
        exitCode = int(exitCode)
        sys.exit(exitCode)
    else:
        print('Error code')
        sys.exit(1)

if __name__ == "__main__":
    main()