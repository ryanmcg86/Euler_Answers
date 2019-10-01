'''A positive integer n is called squarefree, if no square of a prime divides n, 
thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

How many squarefree numbers are there below 2^50?
Link: https://projecteuler.net/problem=193'''

#Imports
import time

#Build a Solve function
def solve(lim):
    #Define variables
    start      = time.time()
    n          = int(lim**0.5)
    moebius    = [1 for i in range(n + 1)]
    sieve      = [False, False] + [True for i in range(2, n + 1)]
    ans        = 0

    #Solve the problem
    for i in range(2, len(sieve)):
        if sieve[i]:
            sieve[i + i::i] = [False] * (n // i - 1)
            square = i**2
            for j in range(i, n + 1, i):
                moebius[j] *= -1
            moebius[square::square] = [0] * (n // square)
        else: continue
	
    for i in range(1, n + 1):
        if moebius[i] == 0: continue
        ans += moebius[i] * (lim / (i**2))
	
    ans = str(ans)
    lim = str(lim)

    #Print the results
    print('There are ' + ans + ' squarefree numbers below ' + lim + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 2**50
solve(lim)
