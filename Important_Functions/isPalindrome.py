'''Returns whether a given input is a palindrome or not (works on numbers or strings)'''

def isPal(n):
    return str(n) == str(n)[::-1]
