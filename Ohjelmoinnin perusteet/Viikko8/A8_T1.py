# A8_T1 Pause
# Create a menu-driven program which has three options:

# Set pause duration
# Activate pause
# Exit
# Utilize time-library’s sleep-function to implement the pause in the program.

# Create a single program file “A8_T1.py”. Use this exercise to build the “template.py” mentioned earlier.
from time import sleep

def showOptions() -> None:
    options = [
        'Set pause duration',
        'Activate pause',  
    ]
    print("Options:")
    item = 0
    for i in options:
        item += 1
        print(f'{item} - {i}')
    print('0 - Exit')

def askChoice() -> int:
    choice = input("Your choice: ")
    try:
        choice = int(choice)
        return choice
    except ValueError:
        return None

def askValue() -> float:
    try:
        value = float(input("Insert pause duration (s): "))
        return value
    except ValueError:
        print("Invalid input.\n")
        return None

def activatePause(duration: float) -> None:
    print(f'Pausing for {duration} seconds.')
    sleep(duration)
    print("Unpaused.\n")

def main() -> None:
    print('Program starting.')
    duration = None
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            duration = askValue()
            print()
        elif choice == 2:
            if duration:
                activatePause(duration)
            else:
                print('Pause is not set.\nSet pause first.\n')
        else:
            print('Unknown option!\n')
    print('Program ending.')

if __name__ == "__main__":
    main()