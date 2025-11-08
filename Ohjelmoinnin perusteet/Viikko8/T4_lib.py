''' This library has funtions for A8_T4
readTimestamps
calculateYears
calculateMonths
calculateWeekday'''

import datetime
from datetime import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    try:
        with open(PFilename) as f:
            for line in f:
                if line == '\n':
                    pass
                else:
                    date_str = line.strip()
                    date_format = '%Y-%m-%dT%H:%M'
                    date_datetime = datetime.strptime(date_str,date_format)
                    PTimestamps.append(date_datetime)
    except IOError:
        print("Invalid filename.")

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    in_year = 0
    for i in range(len(PTimestamps)):
        if PTimestamps[i].year == PYear:
            in_year += 1
    return in_year

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    in_month = 0
    month_num = MONTHS.index(PMonth) + 1
    for i in range(len(PTimestamps)):
        if PTimestamps[i].month == month_num:
            in_month += 1
    return in_month

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    in_weekday = 0
    for i in range(len(PTimestamps)):
        if PTimestamps[i].strftime('%A') == PWeekday:
            in_weekday += 1
    return in_weekday

def main():
    '''Testing functions'''
    filename = 'A8_T4_D2.txt'
    year = 2021
    month = 'October'
    weekday = 'Friday'
    timestamps = []
    readTimestamps(filename, timestamps)
    print(calculateYears(year,timestamps))
    print(calculateMonths(month,timestamps))
    print(calculateWeekdays(weekday,timestamps))

if __name__ == "__main__":
    main()