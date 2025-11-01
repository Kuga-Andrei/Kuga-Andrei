CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ','AJDKSIRUXBLHWTMCQGZNPYFVOE','BDFHJLCPRTXVZNYEIWGAKMUSQO']

user_input = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
encoded_input = ''
positions = [0,0,0]

def position_advance(positions: list[int]) -> None:
    if positions[0] < 25:
        positions[0] += 1
    elif positions[0] == 25 and positions[1] < 25:
        positions[0] = 0
        positions[1] += 1
    elif positions[1] == 25:
        positions[0:1] = 0
        positions[2] += 1


for letter in user_input:
        if letter in CHARACTERS:
            position_advance(positions)
            print(positions)
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

print(encoded_input)
print("MDC BKWPO YDNAY TMC QZJRZ HAPO WRI NLXL VFQ")
