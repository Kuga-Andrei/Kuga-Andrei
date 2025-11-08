# A8_T2 Calculator
# Create a menu-driven program which can perform basic arithmetic operations. All the math operations should be performed with floating datatype and without rounding. Separate the functionality into the appropriate files.

# Recommended subprogram names for the main file:

# def main() -> None:
# def showOptions() -> None:
# def askChoice() -> int:
# def askValue(PPrompt: str) -> float:
# Recommended subprogram names for the library file:

# def add(PAddend1: float, PAddend2: float) -> float:
# def subtract(PMinuend: float, PSubtrahend: float) -> float:
# def multiply(PMultiplicant: float, PMultiplier: float) -> float:
# def divide(PDividend: float, PDivisor: float) -> float:
import T2_lib

def showOptions() -> None:
    options = [
        'Add',
        'Subtract', 
        'Multiply',
        'Divide' 
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

def askValue(PPrompt: str = '') -> float:
    try:
        value = float(input(f"Insert {PPrompt} value: "))
        return value
    except ValueError:
        print("Invalid input.\n")
        return None
    
def main() -> None:
    print('Program starting.')
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            value1 = askValue('first addend')
            value2 = askValue("second addend")
            result = T2_lib.add(value1, value2)
            print(f"{value1} + {value2} = {result}")
            print()
        elif choice == 2:
            value1 = askValue('minuend')
            value2 = askValue("subtrahend")
            result = T2_lib.subtract(value1, value2)
            print(f"{value1} - {value2} = {result}")
            print()
        elif choice == 3:
            value1 = askValue('multiplicand')
            value2 = askValue("multiplier")
            result = T2_lib.multiply(value1, value2)
            print(f"{value1} * {value2} = {result}")
            print()
        elif choice == 4:
            value1 = askValue('dividend')
            value2 = askValue("divisor")
            result = T2_lib.divide(value1, value2)
            print(f"{value1} / {value2} = {result}")
            print()
        else:
            print('Unknown option!\n')
    print('Program ending.')

if __name__ == "__main__":
    main()