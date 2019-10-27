"""
Matthew Yungbluth
Project Euler Problem 45
Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

import time

def main():
    start = time.time()
    for hexa in range(100000000):
        hexnum = (hexa * (2 * hexa - 1))
        pentacount = 1
        pentanum = 1
        tricount = 1
        trinum = 1
        while pentanum < hexnum:
            pentanum = int(pentacount * (3*pentacount - 1)/2)
            pentacount += 1
        while trinum < hexnum:
            trinum = int(tricount * (tricount + 1)/2)
            tricount += 1
        if hexnum == pentanum == trinum:
            print(trinum, tricount, time.time() - start)

main()
