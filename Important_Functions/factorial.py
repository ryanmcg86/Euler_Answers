'''The function to get the factorial of a given input n'''

def factorial(n):
    return factorial(n - 1) * n if n > 1 else 1
