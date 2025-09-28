# A4_T1 For-loop 1
# Create a Python program which prompts user to insert two integers. Use these integers together with the
#  “for-loop” structure to create behaviour like in the example program example run below.

# Note! the autograding tool will test that the correct structure has been applied.
print("Protram starting.\n")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("\nStarting for loop:")
for i in range(start, stop + 1):
    print(i)
print("\nProgram ending.")