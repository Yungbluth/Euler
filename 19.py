"""
Matthew Yungbluth
Project Euler Problem 19
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

def main():
    days = 0
    sundays = 0
    for years in range(100):
        days += 31
        if days % 7 == 0:
            sundays += 1
        if years + 1 % 4 == 0:
            days += 1
        days += 28
        if days % 7 == 0:
            sundays += 1
        days += 31
        if days % 7 == 0:
            sundays += 1
        days += 30
        if days % 7 == 0:
            sundays += 1
        days += 31
        if days % 7 == 0:
            sundays += 1
        days += 30
        if days % 7 == 0:
            sundays += 1
        days += 31
        if days % 7 == 0:
            sundays += 1
        days += 31
        if days % 7 == 0:
            sundays += 1
        days += 30
        if days % 7 == 0:
            sundays += 1
        days += 31
        if days % 7 == 0:
            sundays += 1
        days += 30
        if days % 7 == 0:
            sundays += 1
        days += 31
        if days % 7 == 0:
            sundays += 1
            
    print(sundays)
        

main()
