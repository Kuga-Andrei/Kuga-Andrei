# T3 - Timestamp analysis

# In this task, create a program that reads timestamps from a textfile. The file content is in “.csv” format and contains information related to electricity usage.

# Datasets
# A7_T3_D1.csv
# A7_T3_D2.csv
# A7_T3_D3.csv

# CSV format:

# Has header row
# Columns
#   Weekday
#   Hour
#   Consumption(kWh)
#   Price(€/kWh)
# Separator ;

# Download the datasets to your computer and set up the following steps in your program:

#   Prompt user to insert the filename
#   Read the specified file
#       Skip header row
#       Read line and remove newline character
#       If line is empty (contains only newline character), skip line
#   Analyse timestamps per weekday
#       Count each row that starts with weekday (Row.startswith(…))
#   Display results

# When analysing and creating results, the recommendation is to pass the data rows and the results list to the analyse function. This analyse function then reads the datarows, does the calculations and fills the results list when needed.

# Displaying the results could be a function that simply iterates through the results and displays them. Below is a code example that can help structure the code for the task.

# Preferred datastructures:

# WEEKDAYS: tuple[str]
# Rows: list[str]
# Results: list[str]
# You may run the program with single bash command:

# echo -e "A7_T3_D1.csv\n" | python A7_T3.py

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows = []
    f = open(PFilename, "r")
    f.readline()  # Skip header row
    for row in f:
        if row == '\n':
            continue
        PRows.append(row.rstrip('\n'))
    f.close()
    return PRows

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    WeekdayTimestampAmount= [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(PRows)):
        for j in range(len(WEEKDAYS)):
            if PRows[i].startswith(WEEKDAYS[j]):
                WeekdayTimestampAmount[j] += 1
    for i in range(len(WEEKDAYS)):
        PResults.append((WEEKDAYS[i], WeekdayTimestampAmount[i]))
    WeekdayTimestampAmount.clear()
    return PResults

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    print("### Timestamp analysis ###")
    for i in range(len(PResults)):
        print(f" - {PResults[i][0]} {PResults[i][1]} timestamps")
    print("### Timestamp analysis ###")


def main() -> None:
    print('Program starting.')
    PRows = []
    PResults = []
    filename = input("Insert filename: ")
    PRows = readFile(filename, PRows)
    PResults = analyseTimestamps(PRows, PResults)
    displayResults(PResults)
    PRows.clear()
    PResults.clear()
    print('Program ending.')

if __name__ == "__main__":
    main()