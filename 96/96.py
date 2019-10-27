"""
Matthew Yungbluth
Project Euler Problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle
concept. Its origin is unclear, but credit must be attributed to Leonhard
Euler who invented a similar, and much more difficult, puzzle idea called
Latin Squares. The objective of Su Doku puzzles, however, is to replace the
blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3
box contains each of the digits 1 to 9. Below is an example of a typical
starting puzzle grid and its solution grid.


A well constructed Su Doku puzzle has a unique solution and can be solved by
logic, although it may be necessary to employ "guess and test" methods in
order to eliminate options (there is much contested opinion over this). The
complexity of the search determines the difficulty of the puzzle; the example
above is considered easy because it can be solved by straight forward direct
deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
contains fifty different Su Doku puzzles ranging in difficulty, but all with
unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the
top left corner of each solution grid; for example, 483 is the 3-digit number
found in the top left corner of the solution grid above.
"""

"""
Direct
possibilities
one with only possibility of a number (only 7 in a box possibility)
"""

"""
29' 48' 35'
86' '7' 1'4
'35 ''' 2'9
5'' 12' 4'8
9'3 ''' '(1,2)(1,2,6)
472 ''6 '''
3'1 857 '4'
729 '4' 86'
'84 '1' 5'3

200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003

000000907
000420180
000705026
100904000
050000040
000507009
920108000
034059000
507000000


003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
"""

import sys
import time

def main():
    #if only one box has a num in vert/horiz/box possibility then that is num
    #if multiple boxes have same num can guess by choose then unchoose
    #how to eliminate numbers completely?
    #
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
            if nums[1] == "14":
                booltest = True
            if nums[1] == "15":
                booltest = False
            #sudoku grid is finished, evaluate
            if sudoku != []:
                sudoku = converter(sudoku, booltest)
                finalSum += evaluater(sudoku, booltest)
                print(finalSum)
            #thisSum = evaluater(sudoku)
            #finalSum = finalSum + thisSum
            sudoku = []
        else:
            sudoku.append(list(nums[0]))
    print(finalSum, time.time()-start)
    #sudoku = ["003020600", "900305001", "001806400", "008102900", "700000008",
              #"006708200", "002609500", "800203009", "005010300"]

def converter(sudoku, booltest):
    if booltest:
        print(sudoku)
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == "0":
                sudoku[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                sudoku[i][j] = [int(sudoku[i][j])]
    return sudoku

def evaluater(sudoku, booltest):
    if booltest:
        print(sudoku)
    if len(sudoku[0][0]) == 1 and len(sudoku[0][1]) == 1 and len(sudoku[0][2]) == 1:
        return sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0]
    sudoku = posibilities(sudoku)
    sudoku = chooser(sudoku)
    return evaluater(sudoku, booltest)
    #possibilities

def posibilities(sudoku):
    sudoku = horizontal(sudoku)
    sudoku = vertical(sudoku)
    sudoku = box(sudoku)
    return sudoku

def chooser(sudoku):
    #finds single possibilities on row, column, or box
    sudoku = chooserHoriz(sudoku)
    sudoku = chooserVert(sudoku)
    sudoku = chooserBox(sudoku)
    return sudoku

def chooserHoriz(sudoku):
    for i in range(9):
        posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
        for j in range(9):
            if len(sudoku[i][j]) > 1:
                for posses in sudoku[i][j]:
                    posNumCounter[posses-1][1] += 1
        for a in posNumCounter:
            if a[1] == 1:
                for j in range(9):
                    for posses in sudoku[i][j]:
                        if a[0] == posses:
                            sudoku[i][j] = [a[0]]
                            print(i, j, a[0], "horiz")
                            break
    return sudoku

def chooserVert(sudoku):
    for i in range(9):
        posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
        for j in range(9):
            if len(sudoku[j][i]) > 1:
                for posses in sudoku[j][i]:
                    posNumCounter[posses-1][1] += 1
        for a in posNumCounter:
            if a[1] == 1:
                for j in range(9):
                    for posses in sudoku[j][i]:
                        if a[0] == posses:
                            sudoku[j][i] = [a[0]]
                            print(i, j, a[0], "vert")
                            break
    return sudoku

def chooserBox(sudoku):
    for vert in range(3):
        #horiz*3 for starting point
        for horiz in range(3):
            #vert*3 for starting point
            posNumCounter = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]
            for i in range(3):
                #horiz*3 + i
                for j in range(3):
                    if len(sudoku[vert*3 + i][horiz*3 + j]) > 1:
                        for posses in sudoku[vert*3 + i][horiz*3 + j]:
                            posNumCounter[posses-1][1] += 1
            for a in posNumCounter:
                if a[1] == 1:
                    for i in range(3):
                        for j in range(3):
                            for posses in sudoku[vert*3 + i][horiz*3 + j]:
                                if a[0] == posses:
                                    sudoku[vert*3 + i][horiz*3 + j] = [a[0]]
                                    print(i, j, a[0], "box")
                                    break
    return sudoku

def horizontal(sudoku):
    #if one num left in horizontal then compute that num and add it to sudoku
    #i is rows, j is columns
    for i in range(9):
        numsLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        unsolvedNumsPos = []
        for j in range(9):
            if (len(sudoku[i][j]) == 1) and (sudoku[i][j][0] in numsLeft):
                numsLeft.remove(sudoku[i][j][0])
            else:
                unsolvedNumsPos.append()
        #j unsolvedNumsPos is position of unsolved
        for a in range(len(unsolvedNumsPos)):
            #get possibilities left from num position, if there is a number in possibilities left that isn't in numsLeft, remove it
            currentNumPoss = sudoku[i][unsolvedNumsPos[a]].copy()
            for b in range(len(sudoku[i][unsolvedNumsPos[a]])):
                #currentNumPoss is current possibilities for numbers, unsolvedNumsPos is position of unsolved numbers
                if sudoku[i][unsolvedNumsPos[a]][b] not in numsLeft:
                    currentNumPoss.remove(sudoku[i][unsolvedNumsPos[a]][b])
            sudoku[i][unsolvedNumsPos[a]] = currentNumPoss
    return sudoku

def vertical(sudoku):
    #if one num left in vertical then compute that num and add it to sudoku
    #i is columns, j is rows
    for i in range(9):
        numsLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        unsolvedNumsPos = []
        for j in range(9):
            if (len(sudoku[j][i]) == 1) and (sudoku[j][i][0] in numsLeft):
                numsLeft.remove(sudoku[j][i][0])
            else:
                unsolvedNumsPos.append(j)
        for a in range(len(unsolvedNumsPos)):
            #get possibilities left from num position, if there is a number in possibilities left that isn't in numsLeft, remove it
            currentNumPoss = sudoku[unsolvedNumsPos[a]][i].copy()
            for b in range(len(sudoku[unsolvedNumsPos[a]][i])):
                if sudoku[unsolvedNumsPos[a]][i][b] not in numsLeft:
                    currentNumPoss.remove(sudoku[unsolvedNumsPos[a]][i][b])
            sudoku[unsolvedNumsPos[a]][i] = currentNumPoss
    return sudoku

def box(sudoku):
    #if one num left in box then compute that num and add it to sudoku
    for vert in range(3):
        #horiz*3 for starting point
        for horiz in range(3):
            #vert*3 for starting point
            numsLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            unsolvedNumsPos = []
            for i in range(3):
                #horiz*3 + i
                for j in range(3):
                    #vert*3 + j
                    if (len(sudoku[vert*3 + j][horiz*3 + i]) == 1) and (sudoku[vert*3 + j][horiz*3 + i][0] in numsLeft):
                        numsLeft.remove(sudoku[vert*3 + j][horiz*3 + i][0])
                    else:
                        unsolvedNumsPos.append((vert*3 + j, horiz*3 + i))
            for a in range(len(unsolvedNumsPos)):
            #get possibilities left from num position, if there is a number in possibilities left that isn't in numsLeft, remove it
                thisNum = unsolvedNumsPos[a]
                currentNumPoss = sudoku[thisNum[0]][thisNum[1]].copy()
                for b in range(len(sudoku[thisNum[0]][thisNum[1]])):
                    if sudoku[thisNum[0]][thisNum[1]][b] not in numsLeft:
                        currentNumPoss.remove(sudoku[thisNum[0]][thisNum[1]][b])
                sudoku[thisNum[0]][thisNum[1]] = currentNumPoss
    return sudoku
                    

main()
