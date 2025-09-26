# A3_T7 Decision trees
# In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results. Structure, order and operators matter, so do exactly as the task describes.

# Prompt user to insert value as an integer.
# Display menu
# option 1 - In one multi-branched decision
# option 2 - Independent if-statement decisions
# option 0 - Exit
# Prompt user to choose option
# Apply following math operations in the options 1 & 2
# One multi-branched decision structure:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Independent if-statement decisions one after another:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Exit: “Exiting…”
# At the end of the options 1 & 2, show the results like in the example program runs.
# Other possible output variats:

# “Unknown option.”
print("Program starting.")
print("Testing decision structures.")
value = int(input("Insert an integer: "))
print("Options:\n1 - In one multi-branched decision\n2 - In multiple independent if-statements\n0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    print("Using one multi-branched decision structure.")
    if value >= 400:
        value += 44
    elif value >= 200:
        value += 22
    elif value >= 100:
        value += 11
    print(f"Result is {value}")
elif choice == 2:
    print("Using multiple independent if-statements structure.")
    if value >= 400:
        value += 44
    if value >= 200:
        value += 22
    if value >= 100:
        value += 11
    print(f"Result is {value}")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")