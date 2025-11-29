########################################################
# Task A9_T1
# Developer Andrei Kuga
# Date 2025-11-25
########################################################

# A9_T1 Faulty user input
# Create a Python program that prompts the user to insert floating-point values. If the user inserts 0, stop the prompt and print the sum of the inserted values.

# If the user inserts an invalid value, such as “aaaaa” or “1.b2”, print an error message indicating that the inserted value couldn’t be converted to a floating-point number. Skip the incorrect feed and continue prompting.

# During the prompts, use the raw values for the presentation ("{}".format(Value)). In the final sum presentation, use two decimal presentation format. This can be achieved by using the float format specifier.

# "{:.2f}".format(Value)

# Inputs (for advanced testing):

# Tab 1 Tab 2 Tab 3
# 3.5
# aaaaa
# 1.5
# 0

# Commands to run inputs:

# cat input1.txt | python A9_T1.py
# cat input2.txt | python A9_T1.py
# cat input3.txt | python A9_T1.py

def main():
    print('Program starting.\n')
    inputSum = 0
    while True:
        userInput = input('Insert a floating-point value (0 to stop): ')
        
        try:
            number = float(userInput)
            inputSum += number
            if number == 0:
                break
        except ValueError:
            print("Error! '{}' couldn't be converted to float.".format(userInput))
    print('\nFinal sum is {:.2f}'.format(inputSum))

    print('Program ending.')

if __name__ == "__main__":
    main()