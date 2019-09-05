'''This function returns the number of ways, disregarding order, 
that r objects can be chosen from among n objects. It utilizes the factorial function in Important_Functions'''

#Build a factorial function, 
#which is necessary for an nCr function 
def factorial(n):
    return factorial(n - 1) * n if n > 1 else 1

#Build an nCr function
def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
