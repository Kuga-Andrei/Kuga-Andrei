# A6_T1 Read text file
# Datasets
#   A6_T1_D1.txt
#   A6_T1_D2.txt
#   A6_T1_D3.txt
# Create a program that can read a text file and then print the file content.
# User must be able to specify the file name. Decorate the beginning and the 
# end of the file with a decorative line.

# Decorative lines

# #### START "{filename}" ####
# #### END "{filename}" ####

def read_file(PFileName):
    print(f'#### START "{PFileName}" ####')
    File = open(PFileName)
    while True:
        line = File.readline()
        if line == "":
            print()
            break
        print(line, end="")
    File.close()
    print(f'#### END "{PFileName}" ####')
    return None

def main():
    print("Program starting.")
    print("This program can read a file.")
    FileName = input("Insert filename: ")
    read_file(FileName)
    print("Program ending.")

main()