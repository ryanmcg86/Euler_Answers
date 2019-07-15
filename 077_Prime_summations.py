'''It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
Link: https://projecteuler.net/problem=76'''

#Imports
import time

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

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = 0
    
    #Solve the problem
    for amount in range(10, 100):
        primes = [p for p in range(amount) if isPrime(p)]
        ways = [1] + [0] * amount
        for i in primes:
            for j in range(i, amount + 1):
                ways[j] += ways[j - i]
        if ways[-1] > limit:
            ans = str(amount)
            break
    
    #Print the results
    print 'The first value which can be written as the sum of '
	print 'primes in over ' + str(limit) + ' different ways is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 5000
solve(limit)
