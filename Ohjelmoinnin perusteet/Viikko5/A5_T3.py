# A5_T3 Ask name
# Create a Python program with two functions:

#   main-function
#       Does the routines ("Program starting." and "Program ending.")
#       Utilizes askName-function.
#       Utilizes greetUser-function.
#       Returns None
#   askName-function
#       Prompts the user to insert name
#       Returns name
#   greetUser-function
#       Which takes PName as an argument
#       Greets the user "Hello {PName}!"
#       Returns None
# Note! Tests for this task relies on properly defined functions
# and may fail if the program is not written according to the instructions.
def main():
    print('Program starting.')
    name = askName()
    greetUser(name)
    print('Program ending.')
    return None

def askName():
    Pname = input('Insert name: ')
    return Pname

def greetUser(PName):
    print(f'Hello {PName}!')
    return None

main()
