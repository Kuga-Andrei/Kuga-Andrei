# A4_T3 While-loop
# Make Python program which prompts user to insert two integers. Use these integers
#  together with the “while-loop” structure to create behaviour like in the example program run below.

# Note! the autograding tool will test that the correct structure has been applied.
print("Program starting.\n")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("\nStarting while loop:")
i = start
while i <= stop:
    if i == stop:
        print(i)
    else:
        print(i, end=" ")
    i += 1
print("\nProgram ending.")