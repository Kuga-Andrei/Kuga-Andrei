########################################################
# Task A9_T4
# Developer Andrei Kuga
# Date 2025-11-26
########################################################

EMP_MIN = -273.15
TEMP_MAX = 10000


def collectCelsius() -> None:
    Feed = input('Insert Celsius: ')
    try:
        Feed = float(Feed)
        if Feed < EMP_MIN or Feed > TEMP_MAX:
            raise Exception()
        print('You inserted {:.1f} °C'.format(Feed))
    except ValueError:
        print("Could not convert string to float: '{}'".format(Feed))
    except Exception:
        print('{} temperature out of range.'.format(Feed))
    return Feed

def main():
    print('Program starting.')
    collectCelsius()
    print('Program ending.')

if __name__ == "__main__":
    main()