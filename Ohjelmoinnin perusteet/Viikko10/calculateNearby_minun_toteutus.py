def calculateNearbys(PMineField: list[list[int]]) -> None:
    nearby = 0
    pos = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for row in range(len(PMineField)):
        for col in range(len(PMineField[row])):
            nearby = 0
            if PMineField[row][col] == 9:
                continue
            elif  row == 0:
                if col == 0:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if i[1] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                elif col == len(PMineField[row])-1:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if i[1] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                else:
                    for i in pos:
                        if i[0] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
            elif  row == len(PMineField)-1:
                if col == 0:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if i[1] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                elif col == len(PMineField[row])-1:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if i[1] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                else:
                    for i in pos:
                        if i[0] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
            else:
                if col == 0:
                    for i in pos:
                        if i[1] == -1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                elif col == len(PMineField[row])-1:
                    for i in pos:
                        if i[1] == 1:
                            continue
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
                else:
                    for i in pos:
                        if PMineField[row + i[0]][col + i[1]] == 9:
                            nearby += 1
                    PMineField[row][col] = nearby
    return None