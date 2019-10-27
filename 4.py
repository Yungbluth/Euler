"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def main():
    palindrome = 0
    for i in range(100, 999):
        for j in range(100, 999):
            x = i * j
            palin = True
            p = str(x)
            for y in range(len(p)//2):
                z = y + 1
                if p[y] != p[-z]:
                    palin = False
            if palin == True:
                if x > palindrome:
                    palindrome = x
    print(palindrome)
        
main()
