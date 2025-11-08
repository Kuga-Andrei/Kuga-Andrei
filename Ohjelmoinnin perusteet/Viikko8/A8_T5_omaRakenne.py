# A8_T5 Login and register (TEST TASK)
# Create program which can handle basic user registrations and logins. For this exercise, study the built-in library hashlib. The passwords must be hashed with md5 and hexdigested to a string format. It isn’t necessary to implement unique constraints on usernames.

# Main menu options:

# Login
# Register
# Exit
# User menu options:

# View profile
# Change passsword (no need to implement)
# Logout
# Use “credetials.txt” filename as place to store the credentials in CSV format. The filename can be defined as constant variable on the top-level of the library file. The value separator or delimiter must be a semicolon “;”.

# Example “credentials.txt”:

# 0;admin;58d613129c5e71de57ee3f44c5ce16bc

'''Jäi kesken, palautuksessa piti olla erillainen rakenne'''


import hashlib
DELIMETER = ';'
CREDENTIALS = 'credentials.txt'

def showOptions() -> None:
    options = [
        'Login',
        'Register',  
    ]
    print("Options:")
    item = 0
    for i in options:
        item += 1
        print(f'{item} - {i}')
    print('0 - Exit')

def userMenu() -> None:
    options = [
        'View profile',
        'Change passsword',  
    ]
    print("Options:")
    item = 0
    for i in options:
        item += 1
        print(f'{item} - {i}')
    print('0 - Logout')

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        choice = int(choice)
        return choice
    else:
        return -1

def askUser(PPrompt: str = 'Insert value') -> str:
    value = input(f"{PPrompt}: ")
    return value

def authentication(user: str, password: str) -> bool:
    hex_password = hashlib.md5(b"password").hexdigest()
    with open(CREDENTIALS, "r") as f:
        for line in f:
            line = line.strip().split(DELIMETER)
            if line[1] == user:
                if line[2] == hex_password:
                    return True
        return False

def readValues(filename: str) -> list:
    file_data = []
    try:
        with open(filename) as f:
            for line in f:
                if line == '\n':
                    pass
                else:
                    file_data.append(line.strip())
        return file_data
    except IOError:
        print("Invalid filename.")

def main() -> None:
    print('Program starting.')
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            username = askUser('Insert username')
            password = askUser("Insert password")
            valid = authentication(username, password)
            if valid:
                while True:
                    userMenu()
                    user_choice = askChoice()
                    if user_choice == 0:
                        print('Logging out...\n')
                        username = ''
                        password = ''
                        break
                    elif user_choice == 1:
                        print(f'Profile ID')
        elif choice == 2:
            pass
        else:
            print('Unknown option!\n')
    print('Program ending.')

if __name__ == "__main__":
    main()