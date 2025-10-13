# A6_T4 String analytics
# Datasets
# A6_T4_D1.txt
# A6_T4_D2.txt
# A6_T4_D3.txt
# Create a Python program which is able to analyse names listed in a text file (See dataset files):

# Analyse and specify following aspects from the file:

#   The amount of names
#   Shortest name
#   Longest name
#   Average name length.

# Let the user specify the filename for the analysis. Program reads the file and prints the results
# from the analysis. Values must be presented like shown in the example program runs. Average name 
# length must be presented in 2 decimal precision. Use Format Specification Mini-Language to achieving 
# the required precision for the data presentation.

# Note! Given text files may contain empty rows and the program must be able to skip them if present.

# Other tips:

#    Read text file line-by-line.
#    Pay attention to the reading process (newline characters).
#    Names can be stored into a single string variable.
#       Consider separating names with a semicolon ;
#           John;Doe;Jane
#   Report can be stored into one string variable.
#   Format Specification Mini-Language.
#       E.g., "Value in 2 decimal precision {:.2f}".format(3.555)
def ask_filename():
    filename = input("Insert filename for read: ")
    return filename

def reading_file(file_name):
    with open(file_name, "r") as f:
        print(f'Reading names from "{file_name}".')
        lines = f.readlines()
        names = ";".join(line.strip() for line in lines if line.strip())
    return names

def analyse_names(names):
    print("Analysing names...")
    name_list = names.split(";")
    
    total_names = len(name_list)
    shortest_name = min(name_list, key=len)
    longest_name = max(name_list, key=len)
    average_length = sum(len(name) for name in name_list) / total_names

    print('Analysis complete!')
    print('#### REPORT BEGIN ####')

    print(f"Name count - {total_names}")
    print(f"Shortest name - {len(shortest_name)} chars")
    print(f"Longest name - {len(longest_name)} chars")
    print(f"Average name - {average_length:.2f} chars")
    print('#### REPORT END ####')

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = ask_filename()
    names = reading_file(filename)
    analyse_names(names)
    print("Program ending.")

main()