# A3_T5 Temperature converter (TEST TASK)
# Create a temperature unit conversion program.

# Start the program by listing options for the user:

# Celsius to Fahrenheit
# Fahrenheit to Celsius
# Exit
# Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

# For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

# Data representation examples:

# 50.0 °F
# 10.0 °C
# If the user chooses option Exit, notify the user: Exiting...

# Use 1 decimal precision to round the converted value.
print("Program starting.\n")
print("Options:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius:.1f} °C equals to {fahrenheit:.1f} °F")
elif choice == 2:
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit:.1f} °F equals to {celsius:.1f} °C")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")