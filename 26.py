"""
Matthew Yungbluth
Project Euler Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""
import time
from decimal import *

def main():
    longCycle = 0
    nums = []
    for i in range(1000):
        with localcontext() as context:
            context.prec = 100
            nums.append([])
            num = 1 / Decimal(i + 2).quantize(Decimal(1/(10*100)))
            a = 0
            while num != 0 and a < 100:
                num = (num * 10)
                nums[i].append(int(num // 1))
                num = (num % 1)
                a += 1
    print(nums)
    for num in range(len(nums)):
        if len(nums[num]) == 100:
            print(num)
            
    """
        repeat = False
        top = 1
        a = 1
        num = 1/7
        previousNumer = 0
        prevNumCount = 0
        while not repeat:
            print(num, "1")
            num = num * 10
            print(num, "2")
            numer = int(num // 1)
            if numer == previousNumer:
                prevNumCount += 1
            else:
                previousNumer = numer
            num = num % 1
            print(num, "3")
            print(a, "4")
            if prevNumCount == 3:
                repeat = True
                """

main()
