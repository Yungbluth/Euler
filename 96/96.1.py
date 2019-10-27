
"""

000000907
000420180
000705026
100904000
050000040
000507009
920108000
034059000
507000000

"""
import sys
import time

def main():
    sys.setrecursionlimit(50000)
    start = time.time()
    finalSum = 0
    fopen = open("p096_sudoku.txt")
    sudoku = []
    i = 0
    booltest = False
    for line in fopen:
        nums = line.split()
        if nums[0] == "Grid":
            if nums[1] == "03":
                booltest = True
            if nums[1] == "04":
                booltest = False
            #sudoku grid is finished, evaluate
            if sudoku != []:
                sudoku = converter(sudoku)
                sudoku = initial(sudoku)
                finalSum += evaluater(sudoku, booltest)
                print(finalSum)
            #thisSum = evaluater(sudoku)
            #finalSum = finalSum + thisSum
            sudoku = []
        else:
            sudoku.append(list(nums[0]))
    print(finalSum, time.time()-start)

def converter(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == "0":
                sudoku[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                sudoku[i][j] = int(sudoku[i][j])
    return sudoku

def evaluater(sudoku, booltest):
    #first round populate the possibilities
    #then loop to find single element lists or single possibility in horiz,vert,box
    #when found, convert that list to int of num required
    #update other possibilities according to this new found num
    #search again for another until top 3 have been found
    if type(sudoku[0][0]) is int and type(sudoku[0][1]) is int and type(sudoku[0][2]) is int:
        return sudoku[0][0] + sudoku[0][1] + sudoku[0][2]
    if booltest:
        print(sudoku)
    sudoku = completer(sudoku)
    return evaluater(sudoku, booltest)

def initial(sudoku):
    sudoku = init_horiz(sudoku)
    sudoku = init_vert(sudoku)
    sudoku = init_box(sudoku)
    return sudoku

def init_horiz(sudoku):
    for row in range(9):
        numsToCancel = []
        for column in range(9):
            if type(sudoku[row][column]) is int:
                #populate numsToCancel with all sure numbers
                numsToCancel.append(sudoku[row][column])
        if len(numsToCancel) >= 1:
            for column in range(9):
                if type(sudoku[row][column]) is list:
                    for num in numsToCancel:
                        #removes possibilities
                        if num in sudoku[row][column]:
                            sudoku[row][column].remove(num)
    return sudoku

def init_vert(sudoku):
    for column in range(9):
        numsToCancel = []
        for row in range(9):
            if type(sudoku[row][column]) is int:
                #populate numsToCancel with all sure numbers
                numsToCancel.append(sudoku[row][column])
        if len(numsToCancel) >= 1:
            for row in range(9):
                if type(sudoku[row][column]) is list:
                    for num in numsToCancel:
                        #removes possibilities
                        if num in sudoku[row][column]:
                            sudoku[row][column].remove(num)
    return sudoku

def init_box(sudoku):
    #box*3 + i or j
    for horiz_box in range(3):
        for vert_box in range(3):
            numsToCancel = []
            for horiz_i in range(3):
                for vert_j in range(3):
                    if type(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]) is int:
                        #populate numsToCancel with all sure numbers
                        numsToCancel.append(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j])
            if len(numsToCancel) >= 1:
                for horiz_i in range(3):
                    for vert_j in range(3):
                        if type(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]) is list:
                            for num in numsToCancel:
                                #removes possibilities
                                if num in sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]:
                                    sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j].remove(num)
    return sudoku

def completer(sudoku):
    sudoku = single_poss(sudoku)
    sudoku = only_poss(sudoku)
    sudoku = point_pair(sudoku)
    return sudoku

def point_pair(sudoku):
    #only pair horiz/vert from each other in box with num, eliminate all other
    #   num from row/col respectively
    #only pair in row/col with num, can eliminate all other num from box

    #check in box for horiz or vert pair
    #check to make sure they are the only two/3 in box with that num
    #eliminate that num from poss in row or column

    #check row/col for two/3 pair in same box and nowhere else in row/column
    #eliminate that num from poss in rest of box
    #sudoku = PP_box_horiz(sudoku)
    sudoku = PP_box_vert(sudoku)
    #sudoku = PP_horiz(sudoku)
    sudoku = PP_vert(sudoku)
    return sudoku

def PP_box_horiz(sudoku):
    #checks each box for a horizontal pair/triplet
    #checks rest of box to make sure that possibility doesn't exist in rest of box
    #if so, eliminate that num from possibilities in the rest of the row
    for horiz_box in range(3):
        for vert_box in range(3):
            #each box
            possiblePairs = []
            for horiz_i in range(3):
                #each row in each box
                posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
                for vert_j in range(3):
                    if type(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]) is list:
                        for possibility in sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]:
                            posNumCounter[possibility - 1][1] += 1
                for singlePos in posNumCounter:
                    if singlePos[1] > 1:
                        booltest = True
                        #booltest checks if the pair exists in rest of box
                        for horiz_a in range(3):
                            if True:
                                for vert_b in range(3):
                                    if type(sudoku[horiz_box*3 + horiz_a][vert_box*3 + vert_b]) is list:
                                        for possibility in sudoku[horiz_box*3 + horiz_a][vert_box*3 + vert_b]:
                                            if possibility == singlePos[0]:
                                                booltest = False
                                                
                        if booltest:
                            #this is a PP
                            #row to check is sudoku[horiz_box*3 + horiz_i]
                            for column in range(9):
                                if column//3 != vert_box:
                                    if type(sudoku[horiz_box*3 + horiz_i][column]) is list:
                                        if singlePos[0] in sudoku[horiz_box*3 + horiz_i][column]:
                                            sudoku[horiz_box*3 + horiz_i][column].remove(singlePos[0])
    return sudoku

def PP_box_vert(sudoku):
    #checks each box for a vertical pair/triplet
    #checks rest of box to make sure that possibility doesn't exist in rest of box
    #if so, eliminate that num from possibilities in the rest of the column
    for horiz_box in range(3):
        for vert_box in range(3):
            #each box
            possiblePairs = []
            for vert_j in range(3):
                #each column in each box
                posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
                for horiz_i in range(3):
                    if type(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]) is list:
                        for possibility in sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]:
                            posNumCounter[possibility - 1][1] += 1
                for singlePos in posNumCounter:
                    if singlePos[1] > 1:
                        booltest = True
                        #booltest checks if the pair exists in rest of box
                        for vert_b in range(3):
                            if True:
                                for horiz_a in range(3):
                                    if type(sudoku[horiz_box*3 + horiz_a][vert_box*3 + vert_b]) is list:
                                        for possibility in sudoku[horiz_box*3 + horiz_a][vert_box*3 + vert_b]:
                                            #print(possibility, singlePos[0], possibility == singlePos[0])
                                            if possibility == singlePos[0]:
                                                booltest = False
                                                
                        if booltest:
                            #this is a PP
                            #row to check is sudoku[horiz_box*3 + horiz_i]
                            for row in range(9):
                                if row//3 != horiz_box:
                                    if type(sudoku[row][vert_box*3 + vert_j]) is list:
                                        if singlePos[0] in sudoku[row][vert_box*3 + vert_j]:
                                            sudoku[row][vert_box*3 + vert_j].remove(singlePos[0])
                                            #print("0", row, vert_box*3 + vert_j, singlePos[0])
    return sudoku

def PP_horiz(sudoku):
    #checks each row for a horizontal pair/triplet in the same box
    #checks rest of row to make sure that possibility doesn't exist in rest of row
    #if so, eliminate that num from possibilities in the rest of the box
    for row in range(9):
        posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
        for column in range(9):
            if type(sudoku[row][column]) is list:
                for possibility in sudoku[row][column]:
                    posNumCounter[possibility - 1][1] += 1
        for singlePos in posNumCounter:
            if singlePos[1] > 1:
                booltest = True
                positionone = 11
                for column in range(9):
                    if type(sudoku[row][column]) is list:
                        for possibility in sudoku[row][column]:
                            if possibility == singlePos[0]:
                                if positionone == 11:
                                    positionone = column
                                elif column//3 != positionone//3:
                                    booltest = False
                if booltest:
                    #this is PP
                    #eliminate from rest of box
                    #sudoku[row//3 + horiz_i][positionone + vert_j]
                    for horiz_i in range(3):
                        for vert_j in range(3):
                            if row//3 + horiz_i != row:
                                if type(sudoku[(row//3)*3 + horiz_i][(positionone//3)*3 + vert_j]) is list:
                                    if singlePos[0] in sudoku[(row//3)*3 + horiz_i][(positionone//3)*3 + vert_j]:
                                        sudoku[(row//3)*3 + horiz_i][(positionone//3)*3 + vert_j].remove(singlePos[0])
    return sudoku

def PP_vert(sudoku):
    #checks each column for a vertical pair/triplet in the same box
    #checks rest of column to make sure that possibility doesn't exist in rest of column
    #if so, eliminate that num from possibilities in the rest of the box
    for column in range(9):
        posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
        for row in range(9):
            if type(sudoku[row][column]) is list:
                for possibility in sudoku[row][column]:
                    posNumCounter[possibility - 1][1] += 1
        for singlePos in posNumCounter:
            if singlePos[1] > 1:
                booltest = True
                positionone = 11
                for row in range(9):
                    if type(sudoku[row][column]) is list:
                        for possibility in sudoku[row][column]:
                            if possibility == singlePos[0]:
                                if positionone == 11:
                                    positionone = row
                                else:
                                    if row//3 != positionone//3:
                                        booltest = False
                if booltest:
                    #this is PP
                    #eliminate from rest of box
                    #sudoku[row//3 + horiz_i][positionone//3 + vert_j]
                    for horiz_i in range(3):
                        for vert_j in range(3):
                            if (column//3)*3 + horiz_i != column:
                                if type(sudoku[(positionone//3)*3 + horiz_i][(column//3)*3 + vert_j]) is list:
                                    if singlePos[0] in sudoku[(positionone//3)*3 + horiz_i][(column//3)*3 + vert_j]:
                                        sudoku[(positionone//3)*3 + horiz_i][(column//3)*3 + vert_j].remove(singlePos[0])
                                        #print("1", (positionone//3)*3 + horiz_i, (column//3)*3 + vert_j, singlePos[0])
    return sudoku

def single_poss(sudoku):
    #single possibility for that position
    for row in range(9):
        for column in range(9):
            if type(sudoku[row][column]) is list:
                if len(sudoku[row][column]) == 1:
                    sudoku[row][column] = sudoku[row][column][0]
                    sudoku = eliminate_other_possibilities(sudoku, row, column)
    return sudoku

def eliminate_other_possibilities(sudoku, row, column):
    sudoku = eliminate_horiz(sudoku, row, sudoku[row][column])
    sudoku = eliminate_vert(sudoku, column, sudoku[row][column])
    sudoku = eliminate_box(sudoku, row//3, column//3, sudoku[row][column])
    return sudoku

def only_poss(sudoku):
    #only possibility for that row/column/box
    sudoku = OP_horiz(sudoku)
    sudoku = OP_vert(sudoku)
    sudoku = OP_box(sudoku)
    return sudoku

def OP_horiz(sudoku):
    for row in range(9):
        posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
        for column in range(9):
            if type(sudoku[row][column]) is list:
                for possibility in sudoku[row][column]:
                    posNumCounter[possibility - 1][1] += 1
        for singlePos in posNumCounter:
            if singlePos[1] == 1:
                for column in range(9):
                    if type(sudoku[row][column]) is list:
                        for possibility in sudoku[row][column]:
                            if singlePos[0] == possibility:
                                sudoku[row][column] = singlePos[0]
                                sudoku = eliminate_other_possibilities(sudoku, row, column)
                                if row == 7 and column == 1:
                                    print("1")
                                if row == 7 and column == 2:
                                    print("1.1")
                                #break completely out
                                break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
    return sudoku

def OP_vert(sudoku):
    for column in range(9):
        posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
        for row in range(9):
            if type(sudoku[row][column]) is list:
                for possibility in sudoku[row][column]:
                    posNumCounter[possibility - 1][1] += 1
        for singlePos in posNumCounter:
            if singlePos[1] == 1:
                for row in range(9):
                    if type(sudoku[row][column]) is list:
                        for possibility in sudoku[row][column]:
                            if singlePos[0] == possibility:
                                sudoku[row][column] = singlePos[0]
                                sudoku = eliminate_other_possibilities(sudoku, row, column)
                                if row == 7 and column == 1:
                                    print("2")
                                if row == 7 and column == 2:
                                    print("2.1")
                                #break completely out
                                break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
    return sudoku

def OP_box(sudoku):
    for horiz_box in range(3):
        #horiz*3 for starting point
        for vert_box in range(3):
            #vert*3 for starting point
            posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
            for horiz_i in range(3):
                #horiz_box*3 + horiz_i
                for vert_j in range(3):
                    if type(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]) is list:
                        for possibility in sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]:
                            posNumCounter[possibility - 1][1] += 1
            for singlePos in posNumCounter:
                if singlePos[1] == 1:
                    for horiz_i in range(3):
                        for vert_j in range(3):
                            if type(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]) is list:
                                for possibility in sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]:
                                    if singlePos[0] == possibility:
                                        sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j] = singlePos[0]
                                        sudoku = eliminate_other_possibilities(sudoku, horiz_box*3 + horiz_i, vert_box*3 + vert_j)
                                        if horiz_box == 2 and horiz_i == 1 and vert_box == 0 and vert_j == 1:
                                            print("3")
                                        if horiz_box == 2 and horiz_i == 1 and vert_box == 0 and vert_j == 2:
                                            print("3.1")
                                        break
                                    else:
                                        continue
                                    break
                                else:
                                    continue
                                break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break              
    return sudoku

def eliminate_horiz(sudoku, row, num):
    for column in range(9):
        if type(sudoku[row][column]) is list:
            if num in sudoku[row][column]:
                sudoku[row][column].remove(num)
    return sudoku

def eliminate_vert(sudoku, column, num):
    for row in range(9):
        if type(sudoku[row][column]) is list:
            if num in sudoku[row][column]:
                sudoku[row][column].remove(num)
    return sudoku

def eliminate_box(sudoku, horiz_box, vert_box, num):
    for horiz_i in range(3):
        for vert_j in range(3):
            if type(sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]) is list:
                #removes possibilities
                if num in sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j]:
                    sudoku[horiz_box*3 + horiz_i][vert_box*3 + vert_j].remove(num)
    return sudoku



main()
