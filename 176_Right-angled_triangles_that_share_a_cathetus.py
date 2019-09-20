'''The four right-angled triangles with sides (9,12,15), (12,16,20), (5,12,13) and (12,35,37) all have one of the shorter 
sides (catheti) equal to 12. It can be shown that no other integer sided right-angled triangle exists with one of the catheti 
equal to 12.

Find the smallest integer that can be the length of a cathetus of exactly 47547 different integer sided right-angled triangles.
Link: https://projecteuler.net/problem=176'''

#Imports
import time

#Build a factors function
def factors(n):
    factors = []
    for i in range(2, 4):
        while n % i == 0:
            factors.append(i)
            n /= i
    for i in range(5, int(n**0.5) + 1, 6):
        plus2 = [i, i + 2]
        for j in plus2:
            while n % j == 0:
                factors.append(j)
                n /= j
    if n > 2:
        factors.append(n)
    return factors

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

#Build a Solve function
def solve(number):
    #Define variables
    start = time.time()
    facts = factors(2 * number + 1)
    primes = []
    i = 2
    while len(primes) < len(facts):
        if isPrime(i):
            primes.append(i)
        i += 1
    n = 1

    #Solve the problem
    for d in range(0, len(facts)):
        if d == 0:
            n *= primes[d]**((facts[len(facts) - 1 - d] + 1) / 2)
        else:
            n *= primes[d]**((facts[len(facts) - 1 - d] - 1) / 2)
            
    num = str(number)
    ans = str(n)
        
    #Print the results
    print 'The smallest integer that can be the length of a '
    print 'cathetus exactly ' + num + ' different integer sided '
    print 'right-angled triangles is ' + str(n) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
number = 47547
solve(number)
