'''Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9) = 6.

n   Relatively Prime  φ(n)  n/φ(n)
2   1                 1     2
3   1,2               2     1.5
4   1,3               2     2
5   1,2,3,4           4     1.25
6   1,5               2     3
7   1,2,3,4,5,6       6     1.1666...
8   1,3,5,7           4     2
9   1,2,4,5,7,8       6     1.5
10  1,3,7,9           4     2.5

It can be seen that n = 6 produces a maximum n / φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n / φ(n) is a maximum.
Link: https://projecteuler.net/problem=69'''

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
    multPrimes = 1
    i = 2
    
    #Solve the problem
    while multPrimes <= limit:
        if isPrime(i):
            multPrimes *= i
        if multPrimes > limit:
            multPrimes /= i
            break
        else:
            i += 1

    #Print the results
    print 'The value of n <= ' + str(limit) + ' for which '
    print 'n / phi(n) is a maximum is ' + str(multprimes) + '.'
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 10**6
solve(limit)

'''This was immensely optimized because of some interesting math. Since the goal is to find the 
n value that results in the largest fraction n / phi(n), we need phi(n) to be as small as possible, 
and n to be as big as possible. 

phi(n) is the function that returns the count of distinct relative primes to a given n. 
n / phi(n) can be simplified to be the product of p / (p - 1), where p are each of the primes
that divide into n. For any given n having exactly k distinct prime divisors, n / phi(n) will be largest
when n is divisible by the k smallest primes. 

For example, if n = 30, it has 3 distinct prime divisors, 2, 3, and 5, which happen to be the 3 smallest primes. 
30 / phi(30) = 2 / (2 - 1) * 3 / (3 - 1) * 5 / (5 - 1) = 2 / 1 * 3 / 2 * 5 / 4 = 30 / 8 = 3.75

Similarly, if n = 42, it still has 3 distinct prime divisors, 2, 3, and 7, which are not the 3 smallest primes, 
since 5 is a prime that is less than 7.
42 / phi(42) = 2 / (2 - 1) * 3 / (3 - 1) * 7 / (7 - 1) = 2 / 1 * 3 / 2 * 7 / 6 = 42 / 12 = 3.5

Given that the limit of p / (p - 1) as p approaches infinity = 1, we can see that the larger a prime that is included, 
the closer to 1 its fraction p / (p - 1) gets, and as that gets multiplied into the rest of the fractions made from 
the other distinct primes, it brings the resultant fraction closer to 1, and further away from its potential max.

So, if nk is the product of the k smallest primes, nk / phi(nk) is maximal among all n / phi(n) for n < n(k + 1).
We must therefore find the k with nk <= N < n(k + 1).
For N = 10^6, we find 2 * 3 * 5 * 7 * 11 * 13 * 17 = 510510, hence n7 = 510510 is the correct answer.
'''
