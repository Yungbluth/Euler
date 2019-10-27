"""
Matthew Yungbluth
Project Euler Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import time

def main():
    start = time.time()
    num = "1234567"
    numlist = []
    count = 1
    biggest = 0
    for six in range(7):
        for five in range(6):
            for four in range(5):
                for three in range(4):
                    for two in range(3):
                        for one in range(2):
                            num, count = func(num, 2, count)
                            if int(num) > biggest and is_prime(int(num)):
                                biggest = int(num)
                        num, count = func(num, 3, count)
                        if int(num) > biggest and is_prime(int(num)):
                            biggest = int(num)
                    num, count = func(num, 4, count)
                    if int(num) > biggest and is_prime(int(num)):
                        biggest = int(num)
                num, count = func(num, 5, count)
                if int(num) > biggest and is_prime(int(num)):
                    biggest = int(num)
            num, count = func(num, 6, count)
            if int(num) > biggest and is_prime(int(num)):
                biggest = int(num)
        num, count = func(num, 7, count)
        if int(num) > biggest and is_prime(int(num)):
            biggest = int(num)
    print(biggest,num, time.time() - start)


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
    
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2) // 1) + 1):
        if n % i == 0:
            return False
    return True
    

    
main()
