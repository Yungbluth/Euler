"""
Matthew Yungbluth
Project Euler Problem 56
A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the
maximum digital sum?
"""
import time

def sum_of_num(n):
    finalsum = 0
    for i in range(len(n)):
        finalsum += int(n[i])
    return finalsum
        


def main():
    start = time.time()
    biggest = 0
    for a in range(90, 100):
        for b in range(90, 100):
            x = sum_of_num(str(a**b))
            if x > biggest:
                biggest = x
    print(biggest, time.time()-start)


main()
