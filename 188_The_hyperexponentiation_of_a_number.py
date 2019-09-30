'''The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 and 3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.
Link: https://projecteuler.net/problem=188'''

#Imports
import time

#Build a tetration function
def tetration(a, b, m):
    t0 = 1
    for i in range(b):
        t1 = pow(a, t0, m)
        if t0 == t1: break
        t0 = t1
    return t1

#Build a Solve function
def solve(base, exp, digits):
    #Define variables
    start = time.time()

    #Solve the problem
    ans = str(tetration(base, exp, 10**digits))
        
    b = str(base)
    e = str(exp)
    d = str(digits)

    #Print the results
    print('The last ' + d + ' digits of the hyperexponentiation ')
    print('of ' + b + ' by ' + e + ' are ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
base = 1777
exp = 1855
digits = 8
solve(base, exp, digits)
