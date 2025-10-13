# A6_T6 Cipher messages (TEST TASK)

# Create a Python program which collects plain text rows from user till the user inserts an empty row. 
# Cipher all rows and then ask user to choose between showing the ciphered text or saving it.

# Program must be able to cipher following lowercase and uppercase alphabets. Other characters remains 
# same during ciphering operation.

def collect():
    rows = []
    print("Collecting plain text rows for ciphering.")
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        else:
            rows.append(row)
    return rows

def cipher(plain_text) :
    original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ciphered = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    cipher_list = str.maketrans(original, ciphered)
    secret_text = []
    print('\n#### Ciphered text ####')
    for row in plain_text:
        print(row.translate(cipher_list))
        secret_text.append(row.translate(cipher_list))
    print('\n#### Ciphered text ####')
    return secret_text

def save (secret_text):
    filename = input("Insert filename to save: ")
    if filename == "":
        print('File name not defined.')
        print('Aborting save operation.')
        return None
    else:
        with open(filename, "w") as f:
            for row in secret_text:
                f.write(f'{row}\n')
        print('Ciphered text saved!')
        return None

def main() :
    print("Program starting.\n")
    plain = collect()
    secret = cipher(plain)
    save(secret)
    print("Program ending.")
    
main()
