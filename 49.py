"""
Matthew Yungbluth
Project Euler Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
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
    for i in range(1000, 10000):
        if is_prime(i):
            x = i + 3330
            y = x + 3330
            if is_prime(x) and is_prime(y):
                if sorted(list(str(i))) == sorted(list(str(x))) == sorted(list(str(y))):
                    print(str(i) + str(x) + str(y), time.time() - start)

                    
main()
