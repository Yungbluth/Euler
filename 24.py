"""
Matthew Yungbluth
Project Euler Problem 24
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or
alphabetically, we call it lexicographic order. The lexicographic
permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import sys

def perm():
    """
    get last numbers
    first number += 1
    next numbers in order from smallest to largest
    go until all numbers after 1st are smaller than one before
    """
    num = "0123456789"
    numlist = []
    count = 1
    print(num)
    while count < 100000:
        for nine in range(10):
            for eight in range(9):
                for seven in range(8):
                    for six in range(7):
                        for five in range(6):
                            for four in range(5):
                                for three in range(4):
                                    for two in range(3):
                                        for one in range(2):
                                            num, count = func(num, 2, count)
                                            if count == 1000000:
                                                print(num, count)
                                                sys.exit(1)
                                        num, count = func(num, 3, count)
                                        if count == 1000000:
                                            print(num, count)
                                            sys.exit(1)
                                    num, count = func(num, 4, count)
                                    if count == 1000000:
                                        print(num, count)
                                        sys.exit(1)
                                num, count = func(num, 5, count)
                                if count == 1000000:
                                    print(num, count)
                                    sys.exit(1)
                            num, count = func(num, 6, count)
                            if count == 1000000:
                                print(num, count)
                                sys.exit(1)
                        num, count = func(num, 7, count)
                        if count == 1000000:
                            print(num, count)
                            sys.exit(1)
                    num, count = func(num, 8, count)
                    if count == 1000000:
                        print(num, count)
                        sys.exit(1)
                num, count = func(num, 9, count)
                if count == 1000000:
                    print(num, count)
                    sys.exit(1)
            num, count = func(num, 10, count)
            if count == 1000000:
                print(num, count)
                sys.exit(1)
            print(num, count)
    print(count)
    print(num)


def func(num, ele, count):
    testnum = num
    numlist = []
    for i in range(len(num[-ele:])):
        numlist.append(int(num[-ele + i]))
    x = int(numlist[0]) + 1
    #index of the first element + 1
    if x not in numlist:
        x = int(numlist[0]) + 1
        if x not in numlist:
            x = int(numlist[0]) + 2
            if x not in numlist:
                x = int(numlist[0]) + 3
                if x not in numlist:
                    x = int(numlist[0]) + 4
                    if x not in numlist:
                        x = int(numlist[0]) + 5
                        if x not in numlist:
                            x = int(numlist[0]) + 6
                            if x not in numlist:
                                x = int(numlist[0]) + 7
                                if x not in numlist:
                                    x = int(numlist[0]) + 8
                                    if x not in numlist:
                                        x = int(numlist[0]) + 9

    if x > 9:
        return testnum, count    
    x = numlist.index(x)
    numlist[0], numlist[x] = numlist[x], numlist[0]
    numlist = [numlist[0]] + sorted(numlist[1:])
    tempnum = num[:-ele]
    for j in numlist:
        tempnum += str(j)
    num = tempnum
    if int(testnum) < int(num):
        count += 1
        return num, count
    return testnum, count

"""
    0123
    0132
    0213
    0231
    0312
    0321
"""    

perm()

