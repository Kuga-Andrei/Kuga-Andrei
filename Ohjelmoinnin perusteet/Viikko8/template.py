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
    if choice.isnumeric():
        choice = int(choice)
        return choice
    else:
        return -1

def askValue(PPrompt: str = 'Insert value') -> float:
    try:
        value = float(input(f"{PPrompt}: "))
        return value
    except ValueError:
        print("Invalid input.\n")
        return None

def readValues(filename: str) -> list:
    file_data = []
    try:
        with open(filename) as f:
            for line in f:
                if line == '\n':
                    pass
                else:
                    file_data.append(line.strip())
        return file_data
    except IOError:
        print("Invalid filename.")

def main() -> None:
    print('Program starting.')
    value = None
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            value = askValue()
            print()
        elif choice == 2:
            pass
        else:
            print('Unknown option!\n')
    print('Program ending.')

if __name__ == "__main__":
    main()