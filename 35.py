"""
Matthew Yungbluth
Project Euler Problem 35
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import time

def is_prime(n):
    if n == 1:
        return True
    else:
        booltest = True
        for i in range(2, int(n**(1/2) // 1) + 1):
            if n % i == 0:
                booltest = False
                break
        return booltest
def main():
    start = time.time()
    finalsum = 0
    debug = []
    for i in range(2, 1000000):
        same = set()
        x = str(i)
        booltest = True
        for rot in range(len(x)):
            y = int(x[rot] + x[rot+1:] + x[:rot])
            if y < i:
                booltest = False
        if booltest:
            booltesttwo = True
            for rot in range(len(x)):
                y = int(x[rot] + x[rot+1:] + x[:rot])
                same.add(y)
                if not is_prime(y):
                    booltesttwo = False
                    break
            if booltesttwo:
                finalsum += len(same)
                debug.append(same)
    print(finalsum, debug, time.time() - start)

main()
