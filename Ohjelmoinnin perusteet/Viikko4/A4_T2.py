# A4_T2 For-loop 2
# Copy the previous program and modify the behaviour to match the example program run below. 
# This program must use “for-loop” structure.

# It is recommended to replace the print-command end character with space, so that all the 
# iterations can be printed on the same row. Last iteration might require additional logic 
# to get rid of the extra space at the end.

# Note! the autograding tool will test that the correct structure has been applied.
print("Program starting.\n")   
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("\nStarting for loop:")
for i in range(start, stop + 1):
    if i == stop:
        print(i)
    else:
        print(i, end=" ")
print("\nProgram ending.")