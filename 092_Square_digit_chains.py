'''A number chain is created by continuously adding the square of the 
digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
Link: https://projecteuler.net/problem=92'''

#Imports
import time
from itertools import combinations_with_replacement as cwr

#Build a chain end function
def chain_end(n):
    while n not in [0, 1, 89]:
        n = sum(int(i)**2 for i in str(n))
    return n
    
#Build a factorial function
def fact(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

#Build a solve function
def solve(limit):
    #Define variables
    start     = time.time()
    limlen    = len(str(limit)) - 1 #Limit Length
    numerator = fact(limlen)
    mds       = 9**2 * limlen #Maximum Digit Sum
    ans       = 0
    nums      = [n for n in range(1, mds + 1) if chain_end(n) == 89]

    #Solve the problem	
    for comb in cwr(range(10), limlen):
        if sum(i**2 for i in comb) in nums:
            mults = [comb.count(d) for d in set(comb)]
            denom = 1
            for i in mults:
                denom *= fact(i)
            ans += numerator / denom
    
    #Print the results
    print 'There are ' + str(ans) + ' starting numbers '
    print 'below ' + str(limit) + ' that will arrive at 89.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
limit = 10**7
solve(limit)
