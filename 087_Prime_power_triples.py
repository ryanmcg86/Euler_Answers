'''The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
Link: https://projecteuler.net/problem=87'''

#Imports
import time

#Build an isPrime function
def isPrime(n):
    if n < 2: 
        return False
    if n < 4: 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
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

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    p = []
    for i in range(2, 5):
        p.append(build_sieve(int(limit**(1 / float(i))) + 1))
    nums = set()
    
    #Update sieves with the correct exponents
    for i in range(0, 3):
        p[i] = [p[i][j]**(i + 2) for j in range(len(p[i]))]

    #Solve the problem
    for i in p[0]:
        for j in p[1]:
            for k in p[2]:
                num = i + j + k
                if num < limit:
                    nums.add(num)
                    
    ans = str(len(nums))

    #Print the results
    print 'The amount of numbers that can be expressed as the sum of a prime square, '
    print 'prime cube, and prime fourth power while being less than ' + str(limit) + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
limit = 5 * 10**7
solve(limit)
