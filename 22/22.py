"""
Matthew Yungbluth
Project Euler Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time

def main():
    start = time.time()
    finalsum = 0
    x = open("p022_names.txt")
    names = x.readlines()[0].split(",")
    counter = 1
    for i in sorted(names):
        namesum = 0
        for letter in i[1:-1]:
            namesum += ord(letter.upper()) - 64
        finalsum += namesum * counter
        counter += 1
    print(finalsum, time.time() - start)

main()
