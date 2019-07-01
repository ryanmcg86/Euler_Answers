'''The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
Link: https://projecteuler.net/problem=50'''

#Imports
import time

#Build an isPrime function
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#Build a sieve function
def build_sieve(n):
    if n < 2:
        return []
    if n < 3:
        return [2]
    prime_sieve = [2, 3]
    if n < 5:
        return prime_sieve
    i = 5
    while sum(prime_sieve) <= n:    #We only need up to once the primes sum to n
        if isPrime(i):
            prime_sieve.append(i)
        if isPrime(i + 2) and i + 2 <= n:
            prime_sieve.append(i + 2)
        i += 6
    return prime_sieve

#Build a solve function
def solve(n):
    #Define variables
    start   = time.time()
    primes  = build_sieve(n)
    ans     = 0
    largest = 0
    mpcp    = len(primes) #most possible consecutive primes

    #Calculate the answer
    for i in range(0, mpcp):
        if mpcp - i < largest:
            break
        for j in range(i + 1, mpcp):
            num = sum(primes[k] for k in range(i, j))
            if num > n:
                break
            if isPrime(num) and j - i > largest:
                largest = j - i
                ans = str(num)
            
    #Print the results
    print 'The prime, below ' + str(n) + ', which can be written as the '
    print 'sum of the most consecutive (' + str(largest) + ') primes is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 1000000
solve(n)
