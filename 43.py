"""
Matthew Yungbluth
Project Euler Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import time
import sys

def main():
    perm()

def perm():
    """
    get last numbers
    first number += 1
    next numbers in order from smallest to largest
    go until all numbers after 1st are smaller than one before
    """
    start = time.time()
    num = "0123456789"
    finalsum = 0
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
                                            if divs(num):
                                                finalsum += int(num)
                                        num, count = func(num, 3, count)
                                        if divs(num):
                                            finalsum += int(num)
                                    num, count = func(num, 4, count)
                                    if divs(num):
                                        finalsum += int(num)
                                num, count = func(num, 5, count)
                                if divs(num):
                                    finalsum += int(num)
                            num, count = func(num, 6, count)
                            if divs(num):
                                finalsum += int(num)
                        num, count = func(num, 7, count)
                        if divs(num):
                            finalsum += int(num)
                    num, count = func(num, 8, count)
                    if divs(num):
                        finalsum += int(num)
                num, count = func(num, 9, count)
                if divs(num):
                    finalsum += int(num)
            num, count = func(num, 10, count)
            if divs(num):
                finalsum += int(num)
            print(num, count)
    print(count)
    print(num)
    print(finalsum)
    print(time.time() - start)


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

def divs(n):
    return int(n[1:4]) % 2 == 0 and int(n[2:5]) % 3 == 0 and int(n[3:6]) % 5 == 0 and int(n[4:7]) % 7 == 0 and int(n[5:8]) % 11 == 0 and int(n[6:9]) % 13 == 0 and int(n[7:]) % 17 == 0

    

main()
