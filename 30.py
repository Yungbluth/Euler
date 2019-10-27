"""
Matthew Yungbluth
Project Euler Problem 30
Surprisingly there are only three numbers that can be written as the sum of
powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""
import time

def main():
    start = time.time()
    finalsum = 0
    for i in range(2,500000):
        digits = list(str(i))
        smallsum = 0
        for j in range(len(digits)):
            smallsum += int(digits[j]) ** 5
        if smallsum == i:
            finalsum += i
    print(finalsum, time.time()-start)
        

main()
