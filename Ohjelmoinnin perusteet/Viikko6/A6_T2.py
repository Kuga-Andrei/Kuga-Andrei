# A6_T2 Write text file

# Create a program that can write a text file. Prompt the user to insert first name and last name.
# Then prompt the file name for the write operation. Finally write a text file with first name on
# the first row and last name on the second row. Ensure that the text file ends in a empty row.
# Finally exit the program cleanly.
def ask_user():
    Fname = input("Insert first name: ")
    Lname = input("Insert last name: ")
    FileName = input("Insert filename: ")
    Data = [Fname, Lname, FileName]
    return Data

def write_file(PData):
    new_file = open(PData[2], "w", encoding="utf-8")
    new_file.write(PData[0]+"\n")
    new_file.write(PData[1]+"\n")
    new_file.close()
    return None

def main():
    print("Program starting.")
    Data = ask_user()
    write_file(Data)
    print("Program ending.")

main()