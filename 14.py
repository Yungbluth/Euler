"""
Matthew Yungbluth
Project Euler Problem 14
Which starting number [in the Collatz sequence], under one million,
produces the longest chain?
n → n/2 (n is even)
n → 3n + 1 (n is odd)
"""

def sequence():
    longest = 0
    longestnum = 0
    for i in range(0, 1000000):
        counter = 0
        n = i
        while(n > 1):
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            counter += 1
        if counter > longest:
            longest = counter
            longestnum = i
    print(longestnum)
    

def main():
    sequence()

main()
