# A5_T6 Tally counter (TEST TASK)

# Make a menu-driven Python program which mimics Tally Counter.

# This menu-driven program must contain a maintainable program structure with the following requirements:

# main function which represents the main program logic including menu cycle.
# showOptions function which takes no arguments, shows the available options in the standard output and
# returns None.

# askChoice function which takes no arguments, prompts user to insert choice and returns an integer
# regardless of the user feed.

# In case user incorrectly inserts text as a choice, the program must output "Unknown option!". 

# For this, see the string method isnumeric() behaviour described in W3S or via Python documentation.

# See other requirements in the example program runs below.
def showOptions():
    print('Options:')
    print('1 - Show count')
    print('2 - Increase count')
    print('3 - Reset count')
    print('0 - Exit')
    return None

def askChoice():
    PChoice = input('Your choice: ')
    return PChoice

def main():
    print('Program starting.')
    count = 0
    while True:
        showOptions()
        Choice = askChoice()
        if Choice.isnumeric():
            Choice = int(Choice)
            if Choice == 1:
                print(f'Current count - {count}\n')
            elif Choice == 2:
                count += 1
                print('Count increased!\n')
            elif Choice == 3:
                count = 0
                print('Cleared count!\n')
            elif Choice == 0:
                print('Exiting program.\n')
                break
            else:
                print("Unknown option!\n")
        else:
            print('Unknown option!\n')
    print('Program ending.')

main()