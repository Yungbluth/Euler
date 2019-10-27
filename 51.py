"""
Matthew Yungbluth
Project Euler Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
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
    finalcount = 0
    numcount = 100000
    booltest = True
    while numcount < 1000000:
        finalcount = 0
        if is_prime(numcount):
            count = 0
            x = len(str(numcount))
            num = "0" * x
            while "0" in list(num):
                count += 1
                for i in range(x):
                    if i == 0:
                        if count % (2**(i+1)) == ((2**(i+1))//2):
                            num = num[:-(i + 1)] + "1"
                        if count % (2**(i+1)) == 0:
                            num = num[:-(i + 1)] + "0"
                    else:
                        if count % (2**(i+1)) == ((2**(i+1))//2):
                            num = num[:-(i + 1)] + "1" + num[-i:]
                        if count % (2**(i+1)) == 0:
                            num = num[:-(i + 1)] + "0" + num[-i:]
                #each binary num finished to compare
                one = str(numcount).split()[0]
                two = num.split()[0]
                missed = 0
                smallestmidnum = one
                for replace in range(0, 10):
                    for i in range(len(two)):
                        if two[i] == "1":
                            one = one[:i] + str(replace) + one[i+1:]
                            """
                    midnum = ""
                    for i in one:
                        midnum += i
                        """
                    if not is_prime(int(one)):
                        missed += 1
                    if missed > 2:
                        missed = 4
                        break
                if missed <= 2:
                    print(smallestmidnum, missed, one, two, time.time() - start)
        numcount += 1

def test():
    print(is_prime(109))
    print(is_prime(111109))
    print(is_prime(222109))
    print(is_prime(333109))
    print(is_prime(444109))
    print(is_prime(555109))
    print(is_prime(666109))
    print(is_prime(777109))
    print(is_prime(888109))
    print(is_prime(999109))
test()
"""
1111*
111*1
111**
11*11
binary counter
"""
