# A6_T6 Cipher messages (TEST TASK)

# Create a Python program which collects plain text rows from user till the user inserts an empty row. 
# Cipher all rows and then ask user to choose between showing the ciphered text or saving it.

# Program must be able to cipher following lowercase and uppercase alphabets. Other characters remains 
# same during ciphering operation.

# Required Functions Overview
# Function Name       	            Purpose                 	                Returns

# writeFile(Filename: str,	        Saves the encrypted text to a file          None
# Content: str)                     with the given filename	

# askRows()	                        Asks the user to input multiple lines       A single str containing all rows
#                                   of text (until an empty line is entered)	joined with newline characters

# shiftCharacter(Character: str,    Shifts a character by 13 positions in       A single shifted str character
# Alphabets: str, Shift: int = 13)	the given alphabet
# 	               
# rot13(Content: str)	            Applies the ROT13 cipher to	                A new str with ROT13 applied
#                                   the input string
# main()	                        Runs the full program: input,               None
#                                   ciphering, output, and saving
# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def askRows():
    rows = ""
    print("Collecting plain text rows for ciphering.")
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        else:
            rows += row+"\n"
    return rows

def askFileName():
    filename = input("Insert filename to save: ")
    if filename == "":
        print('File name not defined.')
        print('Aborting save operation.')
        return None
    else:
        return filename

def writeFile(filename, secret_text):
    with open(filename, "w", encoding='UTF-8') as f:
        f.write(secret_text)
    print('Ciphered text saved!')
    return None

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

def showSecret(Secret):
    print('\n#### Ciphered text ####')
    print(Secret)
    print('#### Ciphered text ####')

def main():
    print("Program starting.\n")
    rows = askRows()
    secret = rot13(rows)
    showSecret(secret)
    filename = askFileName()
    if filename:
        writeFile(filename, secret)
    print("Program ending.")

if __name__ == "__main__":
    main()
