########################################################
# Task A10_Tx
# Developer Andrei Kuga
# Date 2025-12-2
########################################################

########################
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston, kun ajaa ohjelman toisesta kansiosta. 
ROOT_DIR = Path(__file__).parent
########################

def main() -> None:
    print('Program starting.\n')
    x = [[9,0,9,0,0,0],[0,0,0,0,0,0],[0,9,0,0,0,0],[9,0,0,0,9,0],[9,0,0,0,0,0],[0,0,0,0,9,9]]
    nearby = 0
    pos = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for i in x:
        print(i)
    print('Nearby marked')
    for row in range(len(x)):
        for col in range(len(x[row])):
            nearby = 0
            if x[row][col] == 9:
                continue
            elif  row == 0:
                if col == 0:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if i[1] == -1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
                elif col == len(x[row])-1:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if i[1] == 1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
                else:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
            elif  row == len(x)-1:
                if col == 0:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if i[1] == -1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
                elif col == len(x[row])-1:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if i[1] == 1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
                else:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
            else:
                if col == 0:
                    for i in pos:
                        if i[1] == -1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
                elif col == len(x[row])-1:
                    for i in pos:
                        if i[1] == 1:
                            continue
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
                else:
                    for i in pos:
                        if x[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    x[row][col] = nearby
    for i in x:
        print(i)
    print('Program ending.')

if __name__ == "__main__":
    main()