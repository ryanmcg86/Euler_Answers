'''The smallest positive integer n for which the numbers n^2 + 1, n^2 + 3, n^2 + 7, n^2 + 9, n^2 + 13, 
and n^2 + 27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
Link: https://projecteuler.net/problem=146'''

#Imports
import time
import random

#Build a mod function
def mods(m):
    res = [True] * m
    add = [1, 3, 7, 9, 13, 27]
    for i in range(0, m):
        for j in range(0, len(add)):
            if ((i * i) + add[j]) % m == 0:
                res[i] = False
                break
    return [i for i in range(len(res)) if res[i]]
    
#Build an isPrime function using Miller-Rabin
def isPrime(n):
    if n in [0, 1, 4, 6, 8, 9]: return False
    if n in [2, 3, 5, 7]: return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert(2**s * d == n - 1)
    
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True
	
    for i in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True
    
#Build an is-Pattern function
def isPat(n):
    add = [1, 3, 7, 9, 13, 27]
    not = [19, 21]
    n2 = n**2
    for i in not:
        if isPrime(n2 + i):
            return False
    for i in add:
        if not isPrime(n2 + i):
            return False
    return True
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = 0
    remainders = [3, 7, 11, 13, 17, 19]
    rems = [mods(i) for i in remainders]
    
    #Solve the problem
    for i in range(10, limit + 1, 10):
        cancel = False
        for j in range(0, len(remainders)):
            if i % remainders[j] not in rems[j]:
                cancel = True
                break
        if cancel: continue
        if isPat(i):
            ans += i

    ans = str(ans)
    lim = str(limit)

    #Print the results
    print 'The sum of all integers below ' + lim + ' that fit '
    print 'the given prime pattern is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 15 * 10**7
solve(limit)
