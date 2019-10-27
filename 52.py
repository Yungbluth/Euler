"""
Matthew Yungbluth
Project Euler Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""
import time

def main():
    start = time.time()
    finalbool = False
    i = 100000
    while not finalbool:
        i += 1
        onelist = sorted(list(str(i)))
        twolist = sorted(list(str(i*2)))
        threelist = sorted(list(str(i*3)))
        fourlist = sorted(list(str(i*4)))
        fivelist = sorted(list(str(i*5)))
        sixlist = sorted(list(str(i*6)))
        finalbool = onelist == twolist == threelist == fourlist == fivelist == sixlist
    print(i, time.time()-start)

def test():
    a = ["1","2","5"]
    b = list("125")
    print(b == a)

main()
