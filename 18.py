"""
Matthew Yungbluth
Project Euler Problem 18
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

TRIANGLE = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


def main():
    """
    Goes from the bottom of the triangle to the top, each time adding
    the largest numbers possible until it gets to the top with the highest
    addition
    """
    for row in range(len(TRIANGLE) - 1, 0, -1):
        for nums in range(len(TRIANGLE[row - 1])):
            bigger = TRIANGLE[row - 1][nums] + TRIANGLE[row][nums]
            biggertwo = TRIANGLE[row - 1][nums] + TRIANGLE[row][nums + 1]
            if bigger > biggertwo:
                TRIANGLE[row - 1][nums] = bigger
            else:
                TRIANGLE[row - 1][nums] = biggertwo
    print(TRIANGLE[0])
            

main()
