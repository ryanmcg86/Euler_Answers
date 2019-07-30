'''In the following equation x, y, and n are positive integers.

(1 / x) + (1 / y) = (1 / n)

For n = 4 there are exactly three distinct solutions:

(1 / 5) + (1 / 20) = (1 / 4)

(1 / 6) + (1 / 12) = (1 / 4)

(1 / 8) + (1 / 8)  = (1 / 4)

What is the least value of n for which the number of distinct solutions exceeds one-thousand?
Link: https://projecteuler.net/problem=108'''

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
    
#Build a build sieve function
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

#Build an exponents of factors function
def exponentsOfFactors(n, primes):
    exp = []
    for i in primes:
        if i > int(n**0.5) + 1:
            break
        counter = 0
        while n % i == 0:
            n /= i
            counter += 1
        if counter > 0:
            exp.append(counter)
    return exp
    
def d(n, primes):
    exp = exponentsOfFactors(n, primes)
    total = 1
    for i in range(len(exp)):
        total *= exp[i] + 1
    return total

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = 1
    primes = build_sieve(int(limit**0.5) + 1)
    
    #Solve the problem
    while (d(ans**2, primes) / 2. > limit) == False:
        ans += 1
    
    ans = str(ans)
    
    #Print the results
    print 'The least value for n for which the number '
    print 'of distinct solutions exceeds ' + str(limit) + ' is ' + ans + '.'   
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 1000
solve(limit)
