# A8_T4 Years, Months and Weekdays
# Create a menu-driven program which is able to read timestamps and count timestamps based on “year”, “month” or “weekday”. Use both provided datasets: “A8_T1D1.txt” and “A8_T1D2.txt”.

# Datasets
# A8_T4_D1.txt
# A8_T4_D2.txt
# For handling the timestamps use the “datetime” library and look for the datetime library documentation aspects:

# strptime and format directives %Y, %m, %d, %H and %M
# year
# month
# day
# Recommended things to implement into the library file:

# MONTHS: list[str] containing month names
# WEEKDAYS: list[str] containing weekday names
# def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
# def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
# def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
# def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
# Weekdays and months can be defined as constant variables in the program top-level. e.g.,
import T4_lib

def showOptions() -> None:
    options = [
        'Calculate amount of timestamps during year',
        'Calculate amount of timestamps during month',
        'Calculate amount of timestamps during weekday'
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

def main() -> None:
    print('Program starting.')
    timestamps = []
    filename = input('Insert filename: ')
    T4_lib.readTimestamps(filename, timestamps)
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            year = int(input("Insert year: "))
            stamps = T4_lib.calculateYears(year,timestamps)
            print(f"Amount of timestamps during year '{year}' is {stamps}\n")

        elif choice == 2:
            month = input("Insert month: ")
            stamps = T4_lib.calculateMonths(month,timestamps)
            print(f"Amount of timestamps during month '{month}' is {stamps}\n")
        elif choice == 3:
            weekday = input("Insert weekday: ")
            stamps = T4_lib.calculateWeekdays(weekday,timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {stamps}\n")
        else:
            print('Unknown option!\n')
    print('Program ending.')

if __name__ == "__main__":
    main()