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

from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            username = askValue("username")
            password = askValue("password")
            authentication = login(username, password)
            if authentication:
                print("Authentication successful!\n")
                userMenu(username)
            else:
                print("Authentication failed!\n")
        elif choice == 2:
            username = askValue("username")
            password = askValue("password")  
            register(username, password)
            print("User registration completed!\n")
        else:
            print('Unknown option!\n')

def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()
        if choice == 0:
            print('Logging out...\n')
            break
        elif choice == 1:
            profile = viewProfile(PUsername)
            print(f'Profile ID {profile[0]} - {profile[1]}\n')
        elif choice == 2:
            new_password = askValue("new password")
            change_password(PUsername, new_password)
            print("Password changed.\n")
        else:
            print('Unknown option!\n')

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        choice = int(choice)
        return choice
    else:
        return -1

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()