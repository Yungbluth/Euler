"""
Matthew Yungbluth
Project Euler Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import time

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def main():
    start = time.time()
    finalsum = 0
    for i in range(10, 50000):
        factsum = 0
        for nums in range(len(str(i))):
            factsum += fact(int(str(i)[nums]))
        if factsum == i:
            finalsum += i
    print(finalsum, time.time() - start)

main()
