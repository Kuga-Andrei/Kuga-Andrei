# A4_T5 Break and continue
# Make a program, which prompts user to insert three integers:

# Starting point
# Stopping point
# Inspection point
# Test the points with following rules(Note! testing order matters):

# Starting point must be less than stopping point
# "Starting point value must be less than the stopping point value."
# The inspection point must be within the range of the start and stop 
# points.
# "Inspection value must be within the range of start and stop."
# If any rule above is broken, print the violation message(s) to the 
# user and then skip the next part till the "Program ending." print.

# Run two for-loops like shown in the example program runs if none of 
# the rules above are broken. Inside the loops, compare the inspection 
# point to the current iteration. Use break and continue commands if the 
# current iteration is same as the inspection point. Otherwise print the 
# current iteration on the same line.

# Note! There must be no trailing space character at the end of any row.
print("Program starting.\n")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
print()
violation = False
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    violation = True
if inspect < start or inspect > stop:
    print("Inspection value must be within the range of start and stop.")
    violation = True
if not violation:
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspect:
            break
        if i < stop-1:
            print(i, end=" ")
        else:
            print(i)
    print("\nSecond loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspect:
            continue
        if i < stop-1:
            print(i, end=" ")
        else:
            print(i)
print("\nProgram ending.")