# T2 - Analyse separated values

# Create a Python program that processes a list of comma-separated integers entered by the user.

# The program will perform the following operations:

#   Parse the input, validate that all entries are valid integers.
#   If an invalid value is detected, output an error message indicating the invalid value, but still process the valid integers.
#   Calculate the sum of the valid integers and determine if the sum is even or odd.
#   Display the total count of valid integers, the sum of the integers, and whether the sum is even or odd.
#   If no valid integers are provided, display an appropriate message.

# Requirements:

#   Input:
#       The user inputs a comma-separated list of values.
#       The program parses these the entered values and checks if they are valid.
#   Output:
#       If all values are valid, display the number of integers, their sum, and whether the sum is even or odd.
#       If invalid values have been entered, display an error message for the invalid value.
#       If no valid integers remain after parsing, inform the user that there are no values to analyze.

# Preferred datastructures: list[int]

def insert():
    user_input = input("Insert comma separated integers: ")
    user_list = user_input.split(",")
    user_num = []
    for user in user_list:
        try:
            num = int(user)
            user_num.append(num)
        except ValueError:
            if user == '':
                pass
            else:
                print(f"Invalid value '{user}' detected.")
    return user_num

def results(user_list):
    len_user = len(user_list)
    if len_user == 0:
        print("No values to analyse.")
        return None
    sum_user = sum(user_list)
    if sum_user % 2 == 0:
        check = "even"
    else:
        check = "odd"

    print(f"There are {len_user} integers in the list.")
    print(f"Sum of the integers is {sum_user} and it's {check}")
    return None


def main():
    print("Program starting.")
    num_list = insert()
    results(num_list)
    print("Program ending.")

if __name__ == "__main__":
    main()