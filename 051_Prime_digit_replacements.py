'''By replacing the 1st digit of the 2-digit number *3, it turns out 
that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the 
ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 
56663, 56773, and 56993. Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
Link: https://projecteuler.net/problem=51'''

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
    i = 5
    while i <= n:
        if isPrime(i):
            prime_sieve.append(i)
        if isPrime(i + 2) and i + 2 <= n:
            prime_sieve.append(i + 2)
        i += 6
    return prime_sieve

#Build a solve function
def solve(n):
    #Define variables
    start = time.time()
    primes = build_sieve(n)
    ans = 0
	
    #Solve the problem
    for prime in primes:
        string_prime = str(prime)
        for n in range(0, len(string_prime)):
            count = 0
            for i in '0123456789':
                permutation = int(string_prime.replace(string_prime[n], i))
                if isPrime(permutation):
                    if permutation >= prime:
                        count += 1
            if count == 8:
                ans = string_prime
                break
        if ans != 0:
            break

    #Print the results
    print 'The smallest prime which, by replacing part of the number '
    print '(not necessarily adjacent digits) with the same digit, '
    print 'is part of an eight prime value family, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 1000000
solve(n)
