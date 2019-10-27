"""
Matthew Yungbluth
Project Euler Problem 36
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

import time

def binary(n):
    #works for n > 1
    exp = 1
    finalnum = "1"
    while (n / 2**exp) >= 2:
        exp += 1
    n -= 2**exp
    #9 = 1001
    #exp + 1 = digits
    for i in range(exp - 1, -1, -1):
        if n / 2**i >= 1:
            finalnum += "1"
            n -= 2**i
        else:
            finalnum += "0"
    return palindrome(finalnum)

def palindrome(x):
    booltest = True
    for j in range(len(x)//2):
        if x[j] != x[-(j+1)]:
            booltest = False
    return booltest

def main():
    start = time.time()
    finalsum = 1
    for i in range(2, 1000000):
        if palindrome(str(i)):
            if binary(i):
                finalsum += i
    print(finalsum, time.time() - start)

main()
