"""
Matthew Yungbluth
Project Euler Problem 28
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""
import time

def main():
    start = time.time()
    add = 1
    for i in range(1, 501):
        x = i * 2 + 1
        for j in range((x-2) * (x-2) + (x - 1), x * x + 1, x - 1):
            add += j
    print(add, time.time() - start)
        

main()



"""
[i-2] step size
keep going until hit i^2
then i += 2
"""
