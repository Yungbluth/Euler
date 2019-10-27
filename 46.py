"""
Matthew Yungbluth
Project Euler Problem 46
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

import time
import sys

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2) // 1) + 1):
        if n % i == 0:
            return False
    return True

def square_loop(i, prime):
    for square in range(1, int(i**(1/2)//1 + 1)):
        if (prime + (2*(square**2))) == i:
            return False
    return True
        

def main():
    start = time.time()
    for i in range(3, 10000, 2):
        booltest = True
        if is_prime(i):
            booltest = False
        else:
            for prime in range(3, i, 2):
                if is_prime(prime):
                    booltest = square_loop(i, prime)
                if booltest == False:
                    break
        if booltest:
            print(i, time.time() - start)
            sys.exit(1)


main()
