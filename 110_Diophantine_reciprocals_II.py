'''In the following equation x, y, and n are positive integers.

1 / x +	1 / y =	1 / n

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for 
which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations 
of a brute force approach it requires a clever implementation.
Link: https://projecteuler.net/problem=110'''

#Imports
import time
from itertools import combinations_with_replacement as cwr

#Build an isPrime function
def isPrime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Build a d function that returns the product of
#the exponents (plus 1) of the prime factors of n
def d(exp):
    total = 1
    for i in range(len(exp)):
        total *= exp[i] + 1
    return total

#Build a solve function
def solve(limit):
    #Declare variables
    start = time.time()
    primes = [2]
    product = 1
    prime = 3
    smallest = limit**2**2
    poss = []

    #Define variables that need defining
    while product < limit**2:
        product = 1
        for j in primes:
            product *= j
        if isPrime(prime):
            primes.append(prime)
        prime += 2
    
    for i in cwr([0, 1, 2, 3, 4, 5], len(primes)):
        exps = []
        for j in range(len(i) - 1, -1, -1):
            exps.append(i[j])
        poss.append(exps)

    #Solve the problem
    for i in range(0, len(poss)):
        temp = []
        for j in range(0, len(poss[i])):
            temp.append(poss[i][j] * 2)
        if d(temp) / 2. > limit:
            ans = 1
            for j in range(0, len(primes)):
                ans *= primes[j]**poss[i][j]
            if ans < smallest:
                smallest = ans

    ans = str(smallest)
    
    #Print the results
    print 'The least value for n for which the number '
    print 'of distinct solutions exceeds ' + str(limit) + ' is ' + ans + '.'   
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 4 * 10**6
solve(limit)
