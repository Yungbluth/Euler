"""
Matthew Yungbluth
Project Euler Problem 53
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
greater than one-million?
"""
import time

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

def main():
    start = time.time()
    millions = 0
    for n in range(1, 101):
        for r in range(1, n):
            if (fact(n) / (fact(r)*fact(n-r))) > 1000000:
                millions += 1
    print(millions, time.time()-start)

main()
