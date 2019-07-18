'''There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10
5C3 = 10.

In general, nCr = n! / r!(n−r)!, where r ≤ n, n! = n × (n−1) × ... × 3 × 2 × 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr for 1 ≤ n ≤ 100, are greater than one-million?
Link: https://projecteuler.net/problem=53'''

#Imports
import time

#Build a factorial function
def fact(n):
    ans = 1
    for i in range(0, n):
        ans *= (i + 1)
    return ans
    
#Build an nCr function
def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    counter = 0
	
    #Solve the problem
    for n in range(1, 101):
        for r in range(1, n + 1):
            if nCr(n, r) > limit:
                counter += 1

    #Print the results
    print 'There are ' + str(counter) + ' values of nCr that are greater'
    print 'than ' + str(limit) + ' for 1 <= n <= 100.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10**6
solve(limit)
