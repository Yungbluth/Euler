"""
Matthew Yungbluth
Project Euler Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

import time

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2) // 1) + 1):
        if n % i == 0:
            return False
    return True


def main():
    start = time.time()
    finalbool = True
    count = 20
    inrow = 0
    while finalbool:
        distinct = set()
        num = count
        while not is_prime(num):
            for i in range(2, num):
                if num % i == 0:
                    distinct.add(i)
                    num = num // i
                    break
        distinct.add(num)
        if len(distinct) == 4:
            inrow += 1
        else:
            inrow = 0
        if inrow == 4:
            finalbool = False
        count += 1
    print(count - 4, time.time() - start)
        

main()
