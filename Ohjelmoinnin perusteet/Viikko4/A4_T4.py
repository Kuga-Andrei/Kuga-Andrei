# A4_T4 Repetitive prompt
# Make a program, which prompts user to insert words. Program must
# stop prompting words if user inserts empty word. After stopping
# the repetitive prompt, print the amount of words and characters
# that the user inserted.
print("Program starting.\n")
word_count = 0
char_count = 0 
while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    word_count += 1
    char_count += len(word)
print(f"\nYou inserted:\n- {word_count} words\n- {char_count} characters\n")
print("Program ending.")