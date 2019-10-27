"""
Matthew Yungbluth
Project Euler Problem 54
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players have a
pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest cards
are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""
import time

VAL_ORDER = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def numcount(newline, testnum):
    count = 0
    for i in range(len(newline)):
        if newline[i] == testnum:
            count += 1
    return count

def biggestnum(newline):
    for i in range(len(VAL_ORDER)-1, 0, -1):
        for j in range(len(newline)):
            if newline[j] == VAL_ORDER[i]:
                return converter(newline[j])

def royalflush(line):
    royalflush = ["T","J","Q","K","A"]
    suit = line[0][1]
    for card in line:
        if card[1] != suit:
            return False
        if card[0] in royalflush:
            royalflush.remove(card[0])
        else:
            return False
    return True
    
def straightflush(line):
    newline = []
    for num in line:
        newline.append(num[0])
    x = straight(newline)
    return (x[0] and flush(line)[0], x[1])

def fourkind(line):
    for i in range(2):
        if numcount(line, line[i]) == 4:
            return (True, converter(newline[i]))
    return (False, 0)

def fullhouse(line):
    x = threekind(line)
    y = twopair(line)
    return (x[0] and y[0],(x[1], y[1]))

def flush(line):
    suit = line[0][1]
    for card in line:
        if card[1] != suit:
            return (False, 0)
    return (True, 0)

def straight(line):
    straighttest = False
    for i in range(0, len(VAL_ORDER)-len(line)):
        if VAL_ORDER[i] in line:
            booltest = True
            for j in range(len(line)-1):
                if VAL_ORDER[i+j+1] not in line:
                    booltest = False
            if booltest:
                straighttest = True
    return (straighttest, biggestnum(line))

def threekind(line):
    for i in range(3):
        if numcount(line, line[i]) == 3:
            return (True, converter(line[i]))
    return (False, 0)
        

def twopair(line):
    pairs = 0
    for i in range(5):
        if numcount(line, line[i]) == 2:
            pairs += 1
    return (pairs == 4, converter(line[i]))

def onepair(line):
    for i in range(5):
        if numcount(line, line[i]) == 2:
            return (True, converter(line[i]))
    return (False, 0)

def converter(n):
    x = n
    if n == "T":
        x = 10
    elif n == "J":
        x = 11
    elif n == "Q":
        x = 12
    elif n == "K":
        x = 13
    elif n == "A":
        x = 14
    return x

def handval(line):
    numline = []
    for num in line:
        numline.append(num[0])
    x = royalflush(line)
    if x:
        return (9, 0)
    x = straightflush(line)
    if x[0]:
        return (8, int(x[1]))
    x = fourkind(numline)
    if x[0]:
        return (7, int(x[1]))
    x = fullhouse(numline)
    if x[0]:
        return (6, int(x[1]))
    x = flush(line)
    if x[0]:
        return (5, int(x[1]))
    x = straight(numline)
    if x[0]:
        return (4, int(x[1]))
    x = threekind(numline)
    if x[0]:
        return (3, int(x[1]))
    x = twopair(numline)
    if x[0]:
        return (2, int(x[1]))
    x = onepair(numline)
    if x[0]:
        return (1, int(x[1]))
    biggest = 0
    for i in numline:
        thisnum = 0
        if i == "A":
            thisnum = 14
        elif i == "K":
            thisnum = 13
        elif i == "Q":
            thisnum = 12
        elif i == "J":
            thisnum = 11
        elif i == "T":
            thisnum = 10
        else:
            thisnum = int(i)
        if thisnum > biggest:
            biggest = thisnum
    return (0, biggest)
        
        

def main():
    start = time.time()
    fopen = open("p054_poker.txt")
    onewin = 0
    for line in fopen:
        line = line.split()
        pone = line[:5]
        ptwo = line[5:]
        handvalone = handval(pone)
        handvaltwo = handval(ptwo)
        if handvalone[0] > handvaltwo[0]:
            onewin += 1
        elif handvalone[0] == handvaltwo[0]:
            if handvalone[1] > handvaltwo[1]:
                onewin += 1
    print(onewin, time.time() - start)
                
                
        
def testone(a):
    return (False, 1)
def test():
    a = 0
    print(testone(a)[0])
    if not testone(a)[0]:
        print("HI")
    if testone(a)[0]:
        print("NO")

main()
