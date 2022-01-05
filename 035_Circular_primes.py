'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
Link: https://projecteuler.net/problem=35'''

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

#Build a build-a-prime-sieve function
def SoE(n): 
    prime = [False] * 2 + [True for i in range(n - 1)]
    ans, p = [], 2
    while p**2 <= n: 
        if prime[p]: 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    for p in range(n + 1): 
        if prime[p]: ans.append(p)
    return ans
    
#Build an isCircular function
def isCircular(n):
    orig = str(n)
    num = orig[1:] + orig[:1]
    prime = isPrime(int(num))
    if not prime: return False
    while prime and num != orig:
        num = num[1:] + num[:1]
        prime = isPrime(int(num))
        if not prime: return False
    return True

#Build a function that simplifys the sieve
#so it only has numbers that don't include
#the digits 0, 2, 4, 5, 6, or 8, as none
#of those can be circular.
def simplify(sieve):
    p = [2, 3, 5, 7]
    for i in range(4, len(sieve)):
        cir, pi = True, sieve[i]
        s = str(pi)
        a, b, c = s.find('0'), s.find('2'), s.find('4')
        d, e, f = s.find('5'), s.find('6'), s.find('8')
        for j in [a, b, c, d, e, f]:
            if j != 1:
                cir = False
                break;
        if cir:
            p.append(pi)
    return p

#Build a Solve function
def solve(num):
    #Define variables
    st = time.time()
    sieve, count = SoE(num), 0
    p = simplify(sieve)
    
    #Solve the problem
    for prime in p:
        if isCircular(prime): count += 1
        
    c, num = str(count), str(num)
    
    #Print the results
    print('There are ' + c + ' circular primes below ' + num + '.')
    print('This took ' + str(time.time() - st) + ' seconds to calculate.')

#Run the program
num = 10**6
solve(num)
