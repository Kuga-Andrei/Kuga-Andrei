import hashlib

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def hash_password(PPassword: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    hash_password = hashlib.md5(PPassword.encode()).hexdigest()
    return hash_password

def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    users = 0
    with open(CREDENTIALS_FILE, "r") as f:
        for line in f:
            line = line.split(DELIMITER)
            if line[0].isnumeric:
                users += 1
    hashPassword = hash_password(PPassword)
    with open(CREDENTIALS_FILE, "a") as f:
        w_line = '{};{};{}\n'.format(users, PUsername, hashPassword)
        f.write(w_line)

def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    hex_password = hash_password(PPassword)
    with open(CREDENTIALS_FILE, "r") as f:
        for line in f:
            line = line.strip().split(DELIMITER)
            if line[1] == PUsername:
                if line[2] == hex_password:
                    return True
        return False

def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    with open(CREDENTIALS_FILE, "r") as f:
        for line in f:
            line = line.strip().split(DELIMITER)
            if line[1] == PUsername:
                userID = line
                return userID
        
def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    file_clone = []
    new_file = []
    #Clone file to list of lines
    with open(CREDENTIALS_FILE, "r") as f:
        for line in f:
            line = line.split(DELIMITER)
            file_clone.append(line)
    HashNewPassword = hash_password(PNewPassword)
    #Search and change User password; copy everything else
    for entry in file_clone:
        if entry[1] == PUsername:
            entry[2] = HashNewPassword+'\n'
            line = DELIMITER.join(entry)
            new_file.append(line)
        else:
            line = DELIMITER.join(entry)
            new_file.append(line)
    
    #Overwrite credentials.txt file
    with open(CREDENTIALS_FILE, "w") as f:
        f.writelines(new_file)