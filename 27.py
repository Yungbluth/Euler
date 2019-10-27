"""
Matthew Yungbluth
Project Euler Problem 27
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer
values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and
certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for
the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601,
is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""
import time
import math

def isprime(n):
    for i in range(2, int(abs(n**(1/2))) // 1 + 1):
        if n % i == 0:
            return False
    return True


def main():
    start = time.time()
    maxprimes = 0
    primesab = [0,0]
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            currentprimes = 0
            for i in range(2, 100000):
                x = i**2 + a*i + b
                if isprime(x):
                    currentprimes += 1
                else:
                    break
            if currentprimes > maxprimes:
                maxprimes = currentprimes
                primesab[0], primesab[1] = a, b
    print("{} primes at n^2 + {}n + {} with a product of {} in {} seconds".format(maxprimes, primesab[0], primesab[1], primesab[0] * primesab[1], time.time()-start))
    

main()