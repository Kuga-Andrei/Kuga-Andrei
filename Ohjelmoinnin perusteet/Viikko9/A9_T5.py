########################################################
# Task A9_T5
# Developer Andrei Kuga
# Date 2025-11-29
########################################################

# A9_T5 RGB (TEST TASK)
# Collect red, green and blue integer values, each on range 0-255 inclusively. This range is often described as “byte” or 8-bit. These 3 bytes (R, G and B) can be used to describe one color using hex notation “#rrggbb”, where the “rr” represents the amount of color red. The hex notation is created using the byte information.

# 28 = 162 = 255

# Above notation:

# 28 - 0-1 * 8 - 8-bits (base2)
# 162 - 0-f * 2 - Hexadecimals (base16)
# 255 - 0-9 0-255 - Integer representation (base10)

# So for example value 127(base-10) converts to 01111111(base-2) in 8-bit format or 7F(base-16) in hexadecimal format.

# While prompting values, ensure that:

# Values are numeric
# Values are actually integers
# Value is inclusively within the 0-255 range
# If any of these conditions aren’t met, then print the error message "Couldn't perform the designed task due to the invalid input values.". Continue the program execution to the end normally skipping the RGB displaying part. One way to achieve this is to use “try-except” for the whole process and then any incorrect value being collected raises exception. See Python Doc: Raising Exceptions

# If the RGB was ok, then show the details like in the example program run. String format specified {:02x} converts integer into 2-digit hex format. More details in the Python Documentation page Format Specification Mini-Language.

# Hex conversion example in Python REPL:

# >>> "#{:02x}{:02x}{:02x}".format(255, 127, 0)
# '#ff7f00'

def askIntByte(PPrompt: str) -> int:
    # Ask for input
    Feed = input(PPrompt)
    if Feed.isnumeric():
        Feed = int(Feed)
        if Feed in range(0,256):
            return Feed
        else:
            print('Value "{}" is out of the range 0-255.'.format(Feed))      
            raise Exception()
    else:
        print('"{}" is non-numeric value.'.format(Feed))
        raise Exception()


def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    hexString = '#{:02x}{:02x}{:02x}'.format(PRed,PGreen,PBlue)
    return hexString

def main():
    print('Program starting.')
    rgb = ['red','green', 'blue']
    inputRGB = []
    try:
        for colour in rgb:
            prompt = 'Insert {}: '.format(colour)
            colour = askIntByte(prompt)
            inputRGB.append(colour)
        hexColour = createHex(inputRGB[0],inputRGB[1],inputRGB[2])
        print('RGB Deatils:')
        for i in range(len(rgb)):
            print('- {} {}'.format(rgb[i],inputRGB[i]))
        print('- Hex {}'.format(hexColour))
        print('- R-byte(base-2): {:08b}'.format(inputRGB[0]))
        print('- G-byte(base-2): {:08b}'.format(inputRGB[1]))
        print('- B-byte(base-2): {:08b}'.format(inputRGB[2]))

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print('Program ending.')

if __name__ == "__main__":
    main()