# A5_T5 Menu-driven program
# Create a menu-driven Python program with following options:

#   Insert a word
#       Which stores user inserted word into memory.
#   Show current word
#       Prints the word from the memory
#   Show current word in reverse
#       Prints the word from the memory in reverse.
#   Exit
#       Stops the program gracefully
#   Unknown option
# Initialize the Word with an empty string.

def menu():
    print('Options:')
    print('1 - Insert word')
    print('2 - Show current word')
    print('3 - Show current word in reverse')
    print('0 - Exit')
    choice = input('Your choice: ')
    return choice

def insert():
    PWord = input('Insert word: ')
    print()
    return PWord

def show(PWord):
    print(f'Current word - "{PWord}"\n')
    return None

def reverse(Pword):
    print(f'Word reversed - "{Pword[::-1]}"\n')
    return None

def main():
    print("Program starting.")
    Word = ""
    while True:
        option = menu()
        option = int(option)
        if option == 1:
            Word = insert()
        elif option == 2:
            show(Word)
        elif option == 3:
            reverse(Word)
        elif option == 0:
            print('Exiting program.\n')
            break
        else:
            print('Unknown option! try again.\n')
    print('Program ending.')

main()

