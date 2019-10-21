'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
Link: https://projecteuler.net/problem=14'''

#Imports
import time
from operator import itemgetter as iget

#Solve function
def solve(lim):
    #Define variables
    start = time.time()
    cache = {1: 1, 2: 2}

    #Solve the problem
    for n in range(3, lim):
        count = 0
        onum = n
        while n > 1:
            if n < onum:
                cache[onum] = cache[n] + count
                break
            if n % 2 == 0: n /= 2
            else: n = 3 * n + 1
            count += 1
            
    ans = str(max(cache.items(), key = iget(1))[0])
    l = str(cache[int(ans)])
    n = str(lim)

    #Print the results
    print('The starting number under ' + n)
    print('with the longest chain is ' + ans + '.')
    print('The chain for ' + ans + ' is ' + l + ' numbers long.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
n = 1000000
solve(n)
