# A5_T2 Pass argument
# Create Python program which is able to print user input with a decorative frame.

# Program must consist of two functions:

#   main-function
#       Print starting and ending statements.
#       Print any empty row (see example program run)
#       Prompt user to insert a word.
#       Pass the inserted word into the frameWord-function.
#       Returns None
#   frameWord
#       Takes PWord as a parameter.
#       Prints the framing and the PWord
#           Hint: Multiply the asterisk '*'-character.
#       Returns None
# Note! Tests for this task relies on properly defined functions and may fail if the
# program is not written according to the instructions.

#Toinen tapa tehdä kehys
#-----------------------------------------------------------------------
# def main():
#     print('Program starting.')
#     word = input('Insert word: ')
#     print()
#     frameWord(word)
#     print('\n\nProgram ending.')
#     return None

# def frameWord(Pword):
#     leveys = len(Pword) + 4
#     rivi = 1
#     while rivi <= 3:
#         if rivi == 2:
#             print('\n*', Pword, '*')
#         else:
#             for x in range(leveys):
#                 print('*', end='')
#         rivi += 1
#     return None
#-----------------------------------------------------------------------

#Yksinkertaisempi kehys
def main():
    print('Program starting.')
    word = input('Insert word: ')
    print()
    framedWord = frameWord(word)
    print(framedWord)
    print('Program ending.')
    return None

def frameWord(Pword):
    framed = '*' * (len(Pword) + 4) + '\n'
    framed = framed + '* ' + Pword + ' *\n'
    framed = framed + '*' * (len(Pword) + 4) + '\n'
    return framed

main()