"""
Matthew Yungbluth
Project Euler Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""
import time
from fractions import Fraction

def main():
    start = time.time()
    finalproduct = 1
    for top in range(10, 99):
        for bottom in range(top + 1, 100):
            numerator = (str(top)[0], str(top)[1])
            denominator = (str(bottom)[0], str(bottom)[1])
            if numerator[1] != "0" and denominator[1] != "0":
                if numerator[0] == denominator[0]:
                    newnum = int(numerator[1]) / int(denominator[1])
                    if newnum == top/bottom:
                        finalproduct *= (int(str(Fraction(newnum).limit_denominator()).split("/")[0])/int(str(Fraction(newnum).limit_denominator()).split("/")[1]))
                elif numerator[0] == denominator[1]:
                    newnum = int(numerator[1]) / int(denominator[0])
                    if newnum == top/bottom:
                        finalproduct *= int(str(Fraction(newnum).limit_denominator()).split("/")[0])/int(str(Fraction(newnum).limit_denominator()).split("/")[1])
                elif numerator[1] == denominator[0]:
                    newnum = int(numerator[0]) / int(denominator[1])
                    if newnum == top/bottom:
                        finalproduct *= int(str(Fraction(newnum).limit_denominator()).split("/")[0])/int(str(Fraction(newnum).limit_denominator()).split("/")[1])
                elif numerator[1] == denominator[1]:
                    newnum = int(numerator[0]) / int(denominator[0])
                    if newnum == top/bottom:
                        finalproduct *= int(str(Fraction(newnum).limit_denominator()).split("/")[0])/int(str(Fraction(newnum).limit_denominator()).split("/")[1])
    print(int(str(Fraction(finalproduct).limit_denominator()).split("/")[1]), time.time() - start)


main()



