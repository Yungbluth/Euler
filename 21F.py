"""
Matthew Yungbluth
Project Euler Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math
import time

def main():
    start = time.time()
    finalsum = 0
    for i in range(1, 10000):
        numsum = 1
        for j in range(2, int(math.sqrt(i) // 1) + 1):
            if i % j == 0:
                numsum += j
                numsum += (i // j)
        numtwosum = 1
        for k in range(2, int(math.sqrt(numsum)) + 1):
            if numsum % k == 0:
                numtwosum += k
                numtwosum += (numsum // k)
        if numtwosum == i:
            if i != numsum and not numsum > 10000:
                finalsum += numsum
    print(finalsum, time.time() - start)
        
main()
