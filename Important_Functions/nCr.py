'''This function returns the number of ways, disregarding order, 
that r objects can be chosen from among n objects. It utilizes the factorial function in Important_Functions'''

#Build an nCr function
def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
