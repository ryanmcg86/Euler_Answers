'''Consider the consecutive primes p1 = 19 and p2 = 23. 
It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, 
there exist values of n for which the last digits are formed by p1 and n is divisible by p2. 
Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
Link: https://projecteuler.net/problem=134'''

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
    
#Build a prime sieve function
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
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = 0
    ps = build_sieve(limit)
    i = ps[len(ps) - 1] + 1
    while isPrime(i) == False:
        i += 1
    ps.append(i)
    
    #Solve the problem
    for i in range(2, len(ps) - 1):
        p1 = ps[i]
        p2 = ps[i + 1]
        lenp1 = len(str(p1))
        r = 10**lenp1 % p2
        if r > 1:
            m = ((p2 - p1) * pow(r, p2 - 2, p2)) % p2
        else:
            m = p2 - p1
        n = m * 10**lenp1 + p1
        ans += n
        
    ans = str(ans)
    limit = str(limit)
        
    #Print the results
    print 'The sum of S for every pair of consecutive primes '
    print 'with 5 <= p1 <= ' + str(limit) + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**6
solve(limit)
