'''Define f(0) = 1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 
using each power no more than twice.

For example, f(10) = 5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10^25)?
Link: https://projecteuler.net/problem=169'''

#Imports
import time

#Build the f(n) function
def f(n, cache):
    if n < 3:            return n
    if cache.has_key(n): return cache[n]
    k = n / 2
    if n % 2 == 1:       res = f((n - 1) / 2, cache)
    else:                res - f(k, cache) + f(k - 1, cache)
    cache[n] =           res
    return res
   
#Build a Solve function
def solve(n):
    #Define variables
    start = time.time()
    cache = {}
    
    #Solve the problem
    ans = str(f(n, cache))
    lim = str(n)

    #Print the results
    print 'When f(n) is the number of different ways n can be expressed '
    print 'as a sum of integer powers of 2 using each power no more than '
    print 'twice, f(' + lim + ') = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 10**25
solve(n)
