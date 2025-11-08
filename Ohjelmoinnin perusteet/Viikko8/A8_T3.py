# A8_T3 Number files
# Create a menu-driven program for analysing number files.

# Datasets
# A8_T3_D1.txt
# A8_T3_D2.txt
# Menu options:

# Read values
# Amount of values
# Calculate sum of values
# Calculate average of values
# The recommendation during the “readValues” operation is to skip the empty rows “\n” and convert the rows into floating point values. Values can be stored into a list[float] data structure.

# The amount of values can be calculated directly by using the “len”- function for the values list. For analysing (options 3 and 4), pass the list of values as an argument to some specific function. After calculating the sum or the average, round the results to one decimal precision. E.g. “1.234” => “1.2”

def showOptions() -> None:
    options = [
        'Read values',
        'Amount of values',
        'Calculate sum of values',
        'Calculate average of values' ,
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

def readValues(filename: str, values) -> list:
    try:
        with open(filename) as f:
            for line in f:
                if line == '\n':
                    pass
                else:
                    line = line.strip()
                    line = float(line)
                    values.append(line)
        return values
    except IOError:
        print("Invalid filename.")

def analyseValues(values: list, option: int) -> float:
    if option == 2:
        result = len(values)
    elif option == 3:
        result = sum(values)
    elif option == 4:
        result = sum(values)/len(values)
    return result

def main() -> None:
    print('Program starting.')
    values = []
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            filename = input('Insert filename: ')
            readValues(filename, values)
            print()
        elif choice == 2:
            result = analyseValues(values, choice)
            print(f'Amount of values {result:.0f}\n')
        elif choice == 3:
            result = analyseValues(values, choice)
            print(f'Sum of values {result:.1f}\n')
        elif choice == 4:
            result = analyseValues(values, choice)
            print(f'Average of {result:.1f}\n')
        else:
            print('Unknown option!\n')
    print('Program ending.')

if __name__ == "__main__":
    main()