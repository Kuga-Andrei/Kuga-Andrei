# A3_T1 If-statements
# Make Python program and implement if-statements in proper places.

# Ask user to insert two integers
# Compare the integers and then announce the greater number
# Create sum of the two integers
# Check the parity of the sum (see modulo-operator ‘%’)
# Other possible output variants:

# Integer comparison
# Integers are the same.
# First integer is greater.
# Parity check
# Sum is even.
print("Program starting.")
print("Insert two integers.")
Int1 = int(input("Insert first integer: "))
Int2 = int(input("Insert second integer: "))

print("Comparing inserted integers.")
if Int1 == Int2:
    print("Integers are the same.")
elif Int1 > Int2:
    print("First integer is greater.")
else:
    print("Second integer is greater.")

Sum = Int1 + Int2
print("\nAdding integers together")
print(Int1, "+", Int2, "=", Sum)

print("\nChecking the parity of the sum...")
if Sum % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")