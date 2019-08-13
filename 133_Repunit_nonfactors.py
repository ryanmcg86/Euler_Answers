'''A number consisting entirely of ones is called a repunit. 
We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Let us consider repunits of the form R(10^n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17. 
Yet there is no value of n for which R(10^n) will divide by 19. 
In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10^n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10n).
Link: https://projecteuler.net/problem=133'''

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
    q = pow(10, 20)
    ans = 5
    ps = build_sieve(limit)[2:]
    
    #Solve the problem
    ans += sum(p for p in ps if pow(10, q, p) != 1)
    ans = str(ans)
        
    #Print the results
    print 'The sum of all the primes below ' + str(limit)
    print 'that will never be a factor of R(10^n) is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**5
solve(limit)
