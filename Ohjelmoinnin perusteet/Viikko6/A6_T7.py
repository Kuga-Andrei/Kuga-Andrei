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

# "player_progress.txt" start
# current_location;next_location;passphrase
# 0;1;qvfpvcyvar

# Player progress file explained:

# 1 First row is the header row with the column names.
# 2 Data row 1
#       1 Current location id 0 refers to the starting point (Home).
#       2 Next location id 1 refers to the next objective (Galba's palace).
#       3 Passphrase ciphered (ROT13)
# 3 Next data row
#       1 Should be added after progress is made on it’s own new line in the same file.
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

# file 1:
# 0;1;qvfpvcyvar
# Cneg 0 - Lrne bs gur Sbhe Rzcrebef:

# Va NQ 68, nsgre Areb'f qrngu, Ebzr cyhatrq vagb punbf.
# Jvgu ab pyrne urve, gur rzcver fnj encvq cbjre fgehttyrf.
# Tnyon gbbx gur guebar svefg, sbyybjrq ol Bgub, Ivgryyvhf, naq svanyyl Irfcnfvna,
# rnpu onggyvat sbe pbageby va jung orpnzr gur Lrne bs gur Sbhe Rzcrebef.

# file 2:
# Part 0 - Year of the Four Emperors:

# In AD 68, after Nero's death, Rome plunged into chaos.
# With no clear heir, the empire saw rapid power struggles.
# Galba took the throne first, followed by Otho, Vitellius, and finally Vespasian,
# each battling for control in what became the Year of the Four Emperors.

# After the progress and the Emperor’s message have been saved, the program closes with the final phrases. 
# The next time the program runs, it should be able to read the previous progress from player_progress.txt 
# and continue the next turn.

# Example program run:

# Travel starting.
# Currently at home.
# Travelling to Galba's palace...
# ...Arriving to the Galba's palace.
# Passing the guard at the entrance.
# "Discipline!"
# Looking for the message in the palace...
# Ah, there it is! Seems cryptic.
# [Game] Progress autosaved!
# Deciphering Emperor's message...
# Looks like I've got now the plain version copy of the Emperor's message.
# Time to leave...
# Travel ending.


LOCATIONS =("home","Galba's palace","Otho's palace","Vitellius' palace","Vespasian's palace")
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def read_progress():
    try:
        with open("player_progress.txt", "r") as f:
            for line in (f.readlines() [-1:]):
                progres_data = line.split(';')
            progres_data[0] = int(progres_data[0])
            progres_data[1] = int(progres_data[1])
            progres_data[2] = progres_data[2].strip()
        return progres_data
    except FileNotFoundError:
        with open("player_progress.txt", "w") as f:
            f.write("current_location;next_location;passphrase\n")
            f.write("0;1;qvfpvcyvar")
            progres_data = [0,1,"qvfpvcyvar"]
            return progres_data

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

def locate_message(next_location, pass_phrase):
    filename = f"{next_location}_{pass_phrase}.gkg"
    with open(filename, "r") as file:
            content = file.read()
            lines = content.strip().split('\n')
            new_progress = lines[0]
            message = '\n'.join(lines[1:])
            return new_progress, message

def append_progress(progress_data):
    with open('player_progress.txt', 'a') as f:
        f.write('\n'+progress_data)

def save_plain(progress_data, plain_passphrase, plain_message):
    filename = f"{progress_data}-{plain_passphrase}.txt"
    with open(filename, "w") as f:
        f.write(plain_message)

def main():
    print("Travel starting.")
    progress = read_progress()
    if progress[1] == 5:
        print('All locations visited.')
        return
    else:
        print(f"Currently at {LOCATIONS[progress[0]]}.")
        print(f"Travelling to {LOCATIONS[progress[1]]}...")
        print(f"...Arriving to the {LOCATIONS[progress[1]]}.")

    print("Passing the guard at the entrance.")
    plain_passphrase = rot13(progress[2])
    print(f'"{plain_passphrase.capitalize()}!"')

    print("Looking for the message in the palace...")
    next_progress, message = locate_message(progress[1], progress[2])
    print("Ah, there it is! Seems cryptic.")

    append_progress(next_progress)
    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    plain_message = rot13(message)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    save_plain(progress[1], plain_passphrase, plain_message)

    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()
