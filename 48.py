"""
Matthew Yungbluth
Project Euler Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

import time

def main():
    start = time.time()
    finalsum = 0
    for i in range(1, 1001):
        finalsum += i**i
    print(str(finalsum)[-10:], time.time() - start)

main()
