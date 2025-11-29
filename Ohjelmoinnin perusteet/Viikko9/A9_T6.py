########################################################
# Task A9_T6
# Developer Andrei Kuga
# Date 2025-11-29
########################################################

# A9_T6 Save before exit (TEST TASK)
# In some scenarios, programs contain unsaved user data, and the user may accidentally do something that typically causes the program to close. In CLI programs, this occurs if the user sends a keyboard interrupt (CTRL + C). Handle the KeyboardInterrupt in a menu-driven program, which collects user-inserted lines.

# If the user has inserted 0 lines during a program run, there is nothing to save. Handle the keyboard interrupt (CTRL + C) smoothly by informing the user that the program is closing suddenly.

# If the user has inserted 1 or more lines and then presses CTRL + C, prompt the user to confirm if they would like to save the lines to a file. If the user confirms with yes, ask for the filename to write. Otherwise close the program gracefully.

# In the example program runs below, keypair ^C indicates user initiated KeyboardInterrupt. Text after ^C on the same line represents program output after keyboard interrupt (color glitch).

########################
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston, kun ajaa ohjelman toisesta kansiosta. 
ROOT_DIR = Path(__file__).parent
########################

def showOptions() -> None:
    print('Options:')
    print('1 - Insert line')
    print('2 - Save lines')
    print('0 - Exit')

def askChoice() -> int:
    try:
        Feed = int(input('Your choice: '))
    except ValueError:
        return -1
    return Feed

def saveLines(PLines: list[str]) -> None:
    filename = input('Insert filename: ')
    fileLocation = ROOT_DIR / filename
    with open(fileLocation, 'w') as f:
        f.writelines(PLines)

def insertLine(PLines: list[str]) -> None:
    line = input('Insert text: ')
    PLines.append(line + '\n')

def onInterrupt(PLines: list[str]) -> None:
    try:
        while True:
            save = input('Save before quit(y/n)?: ')
            if save == 'y':
                saveLines(PLines)
                break
            elif save == 'n':
                break
            else:
                print('Invalid input')
    except KeyboardInterrupt:
        print('n')

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    fileNotSaved = False
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
                fileNotSaved = True
            elif Choice == 2:
                saveLines(Lines)
                fileNotSaved = False
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
        Lines.clear()
    except KeyboardInterrupt:
        if fileNotSaved:
            print('Keyboard interrupt and unsaved progress!')
            onInterrupt(Lines)
        else:
            print('Closing suddenly.')

    print("Program ending.")

if __name__ == "__main__":
    main()