"""
Matthew Yungbluth
Project Euler Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
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
    listofprimes = []
    for i in range(500000):
        if is_prime(i):
            listofprimes.append(i)
    count = 0
    biggestlength = 0
    biggestnum = 0
    while count < len(listofprimes)-count:
        finalsum = 0
        length = 0
        for i in range(len(listofprimes)):
            finalsum += listofprimes[count+i]
            length += 1
            if length > biggestlength:
                if is_prime(finalsum):
                    biggestlength = length
                    biggestnum = finalsum
            if finalsum > 1000000:
                break
        count += 1
    print(biggestlength, biggestnum, time.time()-start)
        
                

main()
