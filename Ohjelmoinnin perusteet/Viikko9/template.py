########################################################
# Task A9_Tx
# Developer Andrei Kuga
# Date 2025-11-25
########################################################

########################
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston, kun ajaa ohjelman toisesta kansiosta. 
ROOT_DIR = Path(__file__).parent
########################



def main():
    print('Program starting.\n')
    print("Couldn't copy \"{}\" to \"{}\".".format('A9_T7_D1.txt','test.txt'))
    print('Program ending.')

if __name__ == "__main__":
    main()