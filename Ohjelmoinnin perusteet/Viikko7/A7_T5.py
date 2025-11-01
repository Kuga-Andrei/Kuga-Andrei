# T5 - Electricity consumption (TEST TASK)
# Analyse provided CSV data and create a summary of daily power usage and cost. Use the data from the A7_T3 task. Rename files accordingly e.g., “A7_T3_D1.csv” => “A7_T5_D1.csv”.

# For the summary, calculate the daily power usage and the cost.

#   Daily usage: Sum the consumption for each timestamp at the daily level. Use gatherer variable.
#   Daily cost: Multiply the consumption by the daily timestamp’s corresponding price. Then sum the results into an gatherer-type variable.
# Preferred datastructures:

#   Timestamps: list[TIMESTAMP]
#   Analysis helper: list[DAY_USAGE]
#   Results: list[str]

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
DELIMITER = ";"

class TIMESTAMP:
    weekday = ''
    hour = ''
    consumption = ''
    price = ''

def readTimestamps(PFilename: str, PTimestamps: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    f = open(PFilename, "r")
    f.readline()  # Skip header row
    for row in f:
        if row == '\n':
            continue
        Row = row.strip()
        Columns = Row.split(DELIMITER)
        Timestamp = TIMESTAMP()
        Timestamp.weekday = Columns[0]
        Timestamp.hour = int(Columns[1])
        Timestamp.consumption = float(Columns[2])
        Timestamp.price = float(Columns[3])
        PTimestamps.append(Timestamp)
    f.close()

def analyseTimestamps(PTimestamps: list[str], PDaily: list[str]) -> None:
    print("Analysing timestamps.")
    daily_usage = [0, 0, 0, 0, 0, 0, 0]
    daily_cost = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(PTimestamps)):
        for j in range(len(WEEKDAYS)):
            if PTimestamps[i].weekday.startswith(WEEKDAYS[j]):
                daily_usage[j] += PTimestamps[i].consumption
                daily_cost[j] += PTimestamps[i].consumption*PTimestamps[i].price
    for i in range(len(WEEKDAYS)):
        PDaily.append((WEEKDAYS[i], daily_usage[i], daily_cost[i]))
    daily_usage.clear()
    daily_cost.clear()

def displayDaily(PDaily: list[str]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for i in range(len(PDaily)):
        print(' - {} usage {:.2f} kWh, cost {:.2f} €'.format(PDaily[i][0], PDaily[i][1], PDaily[i][2]))
    print("### Electricity consumption summary ###") 

def main() -> None:
    print('Program starting.')
    timestamps = []
    daily = []
    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)
    analyseTimestamps(timestamps, daily)
    displayDaily(daily)
    timestamps.clear()
    daily.clear()
    print('Program ending.')

if __name__ == "__main__":
    main()