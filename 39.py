"""
Matthew Yungbluth
Project Euler Problem 39
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import time

def lastnum(a, c, p):
    b = (c**2 - a**2) ** (1/2)
    if b % 1 == 0 and a + b + c == p:
        return True
    return False

def main():
    start = time.time()
    biggestp = 0
    biggestcount = 0
    for p in range(10, 1000):
        count = 0
        for c in range(3, p//2):
            for a in range(1, c):
                if lastnum(a, c, p):
                    count += 1
        if count > biggestcount:
            biggestp = p
            biggestcount = count
    print(biggestp, time.time()-start)

main()
