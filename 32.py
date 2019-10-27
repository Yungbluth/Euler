"""
Matthew Yungbluth
Project Euler Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
import time
import collections

def main():
    start = time.time()
    finalsum = 0
    for i in range(10000):
        testone = collections.Counter(str(i))
        booltestone = True
        for nums in testone:
            if testone[nums] > 1:
                booltestone = False
        if booltestone:
            for divs in range(2, int(i**(1/2) // 1 + 1)):
                if i % divs == 0:
                    testtwo = collections.Counter(str(int(i)) + str(int(divs)) + str(int(i/divs)))
                    booltesttwo = True
                    for nums in testtwo:
                        if testtwo[nums] > 1:
                            booltesttwo = False
                    if booltesttwo and all(k in testtwo for k in ("1","2","3","4","5","6","7","8","9")):
                        finalsum += i
                        break
    print(finalsum, time.time() - start)

main()
