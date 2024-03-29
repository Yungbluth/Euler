"""
Matthew Yungbluth
Project Euler Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def main():
    exp = 2**1000
    num = str(exp)
    newsum = 0
    for i in range(len(num)):
        newsum += int(num[i:i + 1])
    print(newsum)
        

main()
