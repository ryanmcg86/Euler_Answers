'''A row of five grey square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), 
green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.


If green tiles are chosen there are three ways.


And if blue tiles are chosen there are two ways.


Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey tiles in a row measuring five units in length.

How many different ways can the grey tiles in a row measuring fifty units in length be replaced if colours cannot be mixed 
and at least one coloured tile must be used?

NOTE: This is related to Problem 117.
Link: https://projecteuler.net/problem=116'''

#Imports
import time

#Build a factorial function
def factorial(n):
    ans = 1
    for i in range(n, 1, -1):
        ans *= i
    return ans

#Build an nCr function
def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

#Build a solve function
def solve(limit):
    #Declare variables
    start = time.time()
    s = 0
    
    #Solve the problem
    for i in range(2, 5):
        j = 1
        while limit - (i * j) > 0:
            s += nCr(limit - (i * j) + j, j)
            j += 1
            
    ans = str(s + 1)
    
    #Print the results
    print 'In a row measuring ' + str(limit) + ' units in length, the grey tiles '
    print 'can be replaced in ' + ans + ' different ways if colours '
    print 'cannot be mixed and at least one coloured tile must be used.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 50
solve(limit)
