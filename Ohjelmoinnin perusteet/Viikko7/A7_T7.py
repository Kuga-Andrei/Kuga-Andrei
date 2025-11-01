# T7 - Enigma machine
# How did the Enigma Machine work?: https://youtu.be/ybkkiGtJmkM

# Implement Enigma machine in Python.

# The program must handle:

#   3 x Rotors with 26 positions (A-Z)
#   1 x Reflector - Types A, B & C
#   0 x Plugboard. Prompt is required, but no need to implement.
# The order of machine operations described:

#   User presses letter on the keyboard
#       Keypress is passed via plugboard (skipped in this exercise)
#       Rotate the wheels (positions)
#       Scramble current letter using “Forward pass-through” process
#           Iterate through rotors in order 1-3
#               Create offset using current rotor position and the letter
#               Use the offset to shift the given letter in alphabets
#       Scramble current letter using using the reflector
#       Scramble current letter using “Reverse pass-through” process
#           Iterate through rotors in reverse order
#           Change current letter based on each wheel position offset

# In this program, user inserts row and the scrambling starts always from positions [0, 0, 0]. So enter press means that the program must reset the positions before scrambling the inserted text. The Enigma machine will shut down if the user enters an empty line.

# Recommended datastructures:

# Rotors(characters): list[str]
# Positions(rotor positions): list[int]
# Reflector: str

# Initial configs

# Tab 1: iconf1.txt
# Tab 2: iconf2.txt
# Tab 3: iconf3.txt
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def read_config(filename: str, rotors: list[str]) -> str:
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("Rotor"):
                rotor_line = line.split(':')[1]
                rotors.append(rotor_line)
            elif line.startswith("Reflector"):
                reflector = line.split(":")[1]
    return reflector

def position_advance(positions: list[int]) -> None:
    if positions[0] < 25:
        positions[0] += 1
    elif positions[0] == 25 and positions[1] < 25:
        positions[0] = 0
        positions[1] += 1
    elif positions[1] == 25:
        positions[0:1] = 0
        positions[2] += 1

def enigma_cipher(user_input: str, positions: list[int], rotors: list[str], reflector: str) -> str:
    user_input = user_input.upper()
    encoded_input = ''
    for letter in user_input:
        if letter in CHARACTERS:
            position_advance(positions)
            letter_index = CHARACTERS.index(letter)
            for i in range(0,7):
                if i < 3:
                    pos = positions[i]
                    new_letter = CHARACTERS[(letter_index + pos) % 26]
                    letter_index = (rotors[i].index(new_letter) - pos + 26) % 26
        
                elif i == 3:
                    new_letter = reflector[letter_index]
                    letter_index = CHARACTERS.index(new_letter)

                else:
                    pos = positions[3-i]
                    shifted_index = (letter_index + pos) % 26
                    letter_pos = rotors[3-i][shifted_index]
                    letter_index = (CHARACTERS.index(letter_pos) - pos + 26) % 26
            encoded_input += CHARACTERS[letter_index]
        else:
            encoded_input += letter
            pass
    return encoded_input

def show_encoding(user_input, encoded_input):
    for i in range(len(user_input)):
        print('Character "{}" illuminated as "{}"'.format(user_input[i],encoded_input[i]))
    print('Converted row - "{}".\n'.format(encoded_input))

def main():
    filename = input("Insert config(filename): ")
    rotors = []
    reflector = read_config(filename, rotors)
    plugs = input("Insert plugs (y/n)?: ")
    if plugs == 'n':
        print("No extra plugs inserted.")
    else:
        print("Plugboard not implemented.")
    print("Enigma initialized.\n")
    while True:
        user_input = input("Insert row (empty stops): ")
        user_input = user_input.upper()
        positions = [0,0,0]
        if user_input == "":
            print("\nEnigma closing.\n")
            break
        else:
            encoded_input = enigma_cipher(user_input, positions, rotors, reflector)
            show_encoding(user_input, encoded_input)

if __name__ == "__main__":
    main()