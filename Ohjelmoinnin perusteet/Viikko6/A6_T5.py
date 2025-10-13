# A6_T5 Number analytics (TEST TASK)
# Datasets
#   A6_T5_D1.txt
#   A6_T5_D2.txt
#   A6_T5_D3.txt

# Create a program which can analyse numbers in a text file.

# Required values in analysis:

#   Total - integer - Sum of numbers
#   Count - integer - Rows that contain values
#   Greatest - integer - The greatest number of them all
#   Average - decimal - The numbers average
# Think about the processes or “steps” of the analytics first. A prosess which can be described with a name 
# should be wrapped into a function. This function then should only do the task, which belongs to it based on 
# the name. For example if the function name is “readValues”, then the function should read the values from a file. 
# If the function name is “analyseNumbers”, then it should not read a textfile.

# This can be difficult at first with the current know-how, because return statement can only return one value and 
# we have not looked into the datastructures yet. But if you want, you can wrap the values into a string variable 
# using separator in-between the values. This way string can contain multiple values and can be returned as a single 
# value from a function.

# Pseudo-example below:

# SEPARATOR = ";"

# def readValues() -> str:
#   # read operations...
#   Values: str = ""
#   Values += str(13) + SEPARATOR
#   Values += str(45) + SEPARATOR
#   Values += str(20)
#   return Values
# contain only things that the Divide the program structure based on the processes. Define functions to handle 
# the meaningful smaller parts of the program e.g., reading numbers from a given textfiles, analysing numbers 
# and displaying results. Reading values from a file and then storing the values back into a string for the return 
# will help to separate value reading and analysis into their own functionalities.

# This task will not evaluate how well you have structured your code or separated the processes into their own 
# functionalities. But definitely this is a good place to start to consider how robust code are you actually building.

# Present average result in 2 digit precision. Utilize the Format Specification Mini-Language.

# Syntax for 2 digit precision: '{:.2f}'

# Dataset details:

# These datasets contain only positive integer numbers.
# No empty lines. POSIX Line definition
# The results are displayed in CSV format in the example program runs. The first row contains headers, 
# followed by a single data row. Both the column headers and the data values are separated by a semicolon (;). 
# The format is similar to how data is structured in Excel.

# Count	    Sum	    Greatest	Average
# 2	        53	    43	        26.50
SEPARATOR = ";"

def ask_filename():
    """This function asks for filename"""
    filename = input("Insert filename: ")
    filename = filename.strip()
    return filename

def readValues(filename):
    """This function reads values from file and returns them in one string separated by SEPARATOR"""
    lines = ""
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            lines += line + SEPARATOR
    return lines
    
def analyseValues(data):
    """This function analyses string of numbers separated by SEPARATOR and returns results in one string"""
    num_list = data.split(SEPARATOR)
    num_list = [int(x) for x in num_list if x]
    count = len(num_list)
    list_sum = sum(num_list)
    list_great = max(num_list)
    list_avg = list_sum / count
    result = f'Count;Sum;Greatest;Average\n{count};{list_sum};{list_great};{list_avg:.2f}\n'
    return result

def show_result(result, filename):
    """This function prints results"""    
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print(result)
    print("#### Number analysis - END ####")

def main():
    print('Program starting.')    
    filename = ask_filename()
    data = readValues(filename)
    result = analyseValues(data)
    show_result(result, filename)
    print("Program ending.")

if __name__ == "__main__":
    main()