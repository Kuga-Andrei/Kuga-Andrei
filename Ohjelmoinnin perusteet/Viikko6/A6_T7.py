# A6_T7 Messages from the Four Emperors

# Each of the Four Emperors—Galba, Otho, Vitellius and Vespasian—has left a message in their own palaces. 
# Your task is to travel programmatically to each location and gather all their messages.

# You may travel only once per program run. Travel should begin by displaying the current location, followed 
# by the process of traveling to the next location. The first location is the “start” or “Home” location on the 
# map below.

# Place names listed:

# 0 home
# 1 Galba's palace
# 2 Otho's palace
# 3 Vitellius' palace
# 4 Vespasian's palace

# Create a file “player_progress.txt” and initialize it with the following details.

# file 1
# current_location;next_location;passphrase
# 0;1;qvfpvcyvar

# Player progress file explained:

# First row is the header row with the column names.
# Data row 1
#   Current location id 0 refers to the starting point (Home).
#   Next location id 1 refers to the next objective (Galba's palace).
#   Passphrase ciphered (ROT13)
# Next data row
#   Should be added after progress is made on it’s own new line in the same file.
# Once you have traveled to the destination, walk into the palace and shout the passphrase(print the plain version) 
# to the guard as you enter. After entering, locate the message (open file "{NextLocationId}_{PassPhrase}.gkg") and 
# read the content.

# The “.gkg” file extension in this context means that the text file content is in ciphered form. It can be deciphered 
# back to plain text using the Ceasar Cipher (ROT13).

# Read the first line as ciphered text and append it to the player_progress.txt. After the first line, save the plain 
# version of the message into "{NextLocationId}-{PlainPassPhrase}.txt".

# Examples of message formats:

# file1: Ciphered message "{NextLocationId}_{PassPhrase}.gkg"
# file2: Plain version to save "{NextLocationId}-{PlainPassPhrase}.txt"
LOCATIONS =("home","Galba's palace","Otho's palace","Vitellius' palace","Vespasian's palace")
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def progress():
    pass

def shiftCharacter(Character, Alphabets, Shift: int = 13):
    shifted_Alphabets = ''
    for i in range(len(Alphabets)):
        shifted_Alphabets += Alphabets[(i + Shift) % len(Alphabets)]
    cipher_list = str.maketrans(Alphabets, shifted_Alphabets)
    shifted_char = Character.translate(cipher_list)
    return shifted_char

def rot13(Content):
    shifted_Content = ''
    for i in Content:
        if i.isupper(): 
            shifted_Content += shiftCharacter(i, UPPER_ALPHABETS)
        else:
            shifted_Content += shiftCharacter(i, LOWER_ALPHABETS)
    return shifted_Content

def locate_message():
    pass

def append_progress():
    pass

def save_plain():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
