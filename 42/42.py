"""
Matthew Yungbluth
Project Euler Problem 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""

import time

def main():
    start = time.time()
    trilist = []
    count = 0
    for n in range(1, 20):
        trilist.append(int((1/2)*n*(n+1)))
    fopen = open("42.txt")
    for readfile in fopen:
        wordlist = readfile.strip("\"").split("\",\"")
    for word in wordlist:
        value = 0
        for character in word:
            value += ord(character)-64
        if value in trilist:
            count += 1
    print(count, time.time() - start)

main()
