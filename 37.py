"""
Matthew Yungbluth
Project Euler Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
    finalsum = 0
    count = 0
    finallist = []
    for i in range(999999, 9, -2):
        booltest = True
        x = str(i)
        for left in range(len(x)):
            if not is_prime(int(x[left:])):
                booltest = False
                break
        if booltest:
            for right in range(len(x)-1, 0, -1):
                if not is_prime(int(x[0:right])):
                    booltest = False
                    break
        if booltest:
            count += 1
            finalsum += i
            finallist.append(x)
        if count == 11:
            break
    print(finalsum, count, finallist, time.time()-start)


main()
