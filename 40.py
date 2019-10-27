"""
Matthew Yungbluth
Project Euler Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

import time

def main():
    start = time.time()
    big = ""
    count = 1
    while len(big) < 1000000:
        big += str(count)
        count += 1
    final = int(big[0]) * int(big[9]) * int(big[99]) * int(big[999]) * int(big[9999]) * int(big[99999]) * int(big[999999])
    print(final, time.time()-start)
main()
