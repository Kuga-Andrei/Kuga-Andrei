# A3_T2 String comparisons
# Make Python program which does the following steps:

# Prompt user to insert
# A word
# A character
# Find if the character exists in the word. Possible prints below.
# Word "{WordFirst}" contains character "{Character}"
# Word "{WordFirst}" doesn't contain character "{Character}"
# Prompt user to insert one more word
# Compare the first word to the second word. Examples below:
# The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
# The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
# Both inserted words are the same alphabetically, "{WordFirst}"
print("Program starting.")
print("String comparison")
WordFirst = input("Insert first word: ")
Character = input("Insert a character: ")
if Character in WordFirst:
    print(f'Word "{WordFirst}" contains character "{Character}"')
else:
    print(f'Word "{WordFirst}" doesn\'t contain character "{Character}"')
WordSecond = input("Insert second word: ")
if WordFirst == WordSecond:
    print(f'Both inserted words are the same alphabetically, "{WordFirst}"')
elif WordFirst < WordSecond:
    print(f'The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.')
else:
    print(f'The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.')
print("Program ending.")