# A4_T7 Multiplicative persistency (TEST TASK)
# Create program which prompts the user to insert an 
# integer and then display the steps to calculate the 
# multiplicative persistency based on the user input.

# In short, the steps in the multiplicative persistency 
# is calculated by multiplying digits together in a given 
# integer. This process is then repeated for the result which 
# makes the result value smaller on each iteration till the result 
# contains only one digit.

# The program must stop the iteration when the result contains 
# only one digit. Finally before the program closes, it shows 
# the steps taken.
print("Program starting.\n")
print("Check multiplicative persistence.")
number = input("Insert an integer: ")
step = 0
while len(number) > 1:
    step += 1
    result = 1
    kierros = 0
    for digit in number:
        result *= int(digit)
        kierros += 1
        if kierros == len(number):
            print(digit, end=" ")
        else:
            print(digit, end=" * ")
    print(f"= {result}")
    number = str(result)
print("No more steps.\n")
print(f"This program took {step} step(s)")
print("\nProgram ending.")