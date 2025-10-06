# A6_T3 Copy text file

# Create a program that copies a text file by reading from a source file and writing the 
# content to a destination file. Allow the user to specify the source and destination file names.
def ask_files():
    source_name = input("Insert source filename: ")
    destination_name = input("Insert destination filename: ")
    return source_name, destination_name

def reading_file(FileName):
    print(f"Reading file '{FileName}' content.")
    reading_file = open(FileName, "r")
    Data = reading_file.read()
    reading_file.close()
    print("File content ready in memory.")
    return Data

def writing_file(FileName, Data):
    print(f"Writing content into file '{FileName}'.")
    writing_file = open(FileName, "w")
    writing_file.write(Data)
    writing_file.close()
    print("Copying operation complete.")
    return None

def main():
    print("Program starting.")
    print("This program can copy a file.")
    sfile, dfile = ask_files()
    sdata =reading_file(sfile)
    writing_file(dfile, sdata)
    print("Program ending.")

main()
