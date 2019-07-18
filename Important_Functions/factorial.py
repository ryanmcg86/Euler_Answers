'''The function to get the factorial of a given input n'''

def factorial(n):
    ans = 1
    for i in range(n, 1, -1):
        ans *= i
    return ans
