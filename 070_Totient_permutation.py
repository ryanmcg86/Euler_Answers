'''Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number 
of positive numbers less than or equal to n which are relatively prime to n. For example, 
as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9) = 6.
The number 1 is considered to be relatively prime to every positive number, so φ(1) = 1.

Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n / φ(n) produces a minimum.
Link: https://projecteuler.net/problem=70'''

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
    
#Build a build_sieve function
def build_sieve(n):
    if n < 2: return []
    if n < 3: return [2]
    ps = [2, 3]
    i = 5
    while i <= n:
        if isPrime(i): ps.append(i)
        m = i + 2
        if m > n: break
        if isPrime(m): ps.append(m)
        i += 6
    return ps

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    length = len(str(int(limit**0.5)))
    ps = build_sieve(10**length)
    minNphi = limit
    ans = 0
    
    #Solve the problem
    for prime1 in ps:
        for prime2 in ps:
            num = prime1 * prime2
            if num > limit or prime1 == prime2:
                break
            phi = (prime1 - 1) * (prime2 - 1)
            nPhi = num / float(phi)
            if nPhi < minNphi:
                if sorted(str(num)) == sorted(str(phi)):
                    ans = num
                    minNphi = nPhi

    #Print the results
    print 'The value of n, where 1 < n < ' + str(limit) + ', for which phi(n) is a '
    print 'permutation of n and the ratio n / phi(n) produces a minimum, is ' + str(ans) + '.'
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 10**7
solve(limit)

'''This was immensely optimized because of some interesting math. Since the goal is to find the 
n value that results in the smallest fraction n / phi(n), we need phi(n) to be as close to n as possible, 
and n to be as big as possible. 

phi(n) is the function that returns the count of distinct relative primes to a given n. 
When n is prime, phi(n) = n - 1, as all numbers between 1 and n - 1 are relatively prime to n, by definition 
of primality.

We know that n - 1 can never be a permutation of n, so the answer cannot be prime. The next best method is
to test numbers that are the product of 2 primes. Since we're using the product of primes, we can calculate
phi(n) as simply (i - 1) * (j - 1) where i and j are the 2 non-equal primes that multiply to n.

To save further time, we only need to check whether these prime-products' phi results are proper permutations 
when the resultant (i * j) / ((i - 1) * (j - 1)) is less than the current minimum value for n / phi(n).


'''
