"""
Matthew Yungbluth
Project Euler Problem 23
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.

4179871
"""

import math
import time

def main():
    start = time.time()
    abundantnums = []
    finalnums = []
    finalsum = 0
    for abuns in range(11, 28124):
        finalnums.append(True)
        sumdivs = 0
        for divs in range(2, int(math.sqrt(abuns) // 1) + 1):
            if abuns % divs == 0:
                sumdivs += divs
                if abuns / divs != divs:
                    sumdivs += (abuns // divs)
        if sumdivs > abuns:
            abundantnums.append(abuns)
    x = len(abundantnums)
    y = len(finalnums)
    for i in range(x):
        for j in range(i, x):
            z = abundantnums[i] + abundantnums[j]
            if y > z:
                finalnums[z] = False
    for a in range(y):
        if finalnums[a] == True:
            finalsum += a
    print(finalsum, time.time() - start)
            

main()
