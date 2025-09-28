# A4_T6 Collatz Conjecture (TEST TASK)
# Create a program which prompts the user to insert an integer and
# then display the collatz conjecture.
# The collatz conjecture is defined as follows:
# Start with any positive integer n.
# If the number is even, divide it by two.
# If the number is odd, triple it and add one.
# Repeat this process until the number is one.
# Print the number of steps taken to reach one.

print("Program starting.")
number = int(input("Insert a positive integer: "))
steps = 0
if number <= 0:
    print("The number must be positive.")
else:
    while number != 1:
        print(number, end=" -> ")
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        steps += 1
    print(1)
print(f"Sequence had {steps} total steps.\n")
print("Program ending.")