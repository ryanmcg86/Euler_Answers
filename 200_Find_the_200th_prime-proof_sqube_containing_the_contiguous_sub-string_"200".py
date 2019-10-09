'''We shall define a sqube to be a number of the form, p^2 * q^3, where p and q are distinct primes.
For example, 200 = 5^2 * 2^3 or 120072949 = 23^2 * 61^3.

The first five squbes are 72, 108, 200, 392, and 500.

Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; 
we shall call such numbers, prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.

Find the 200th prime-proof sqube containing the contiguous sub-string "200".
Link: https://projecteuler.net/problem=200'''

#Imports
import time

#Build a dumb isPrime function
def isPrime_dumb(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Build a Sieve of Eratosthenes function
def SoE(n):
    prime = [True for i in range(n + 1)]
    ans, p = [], 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] == False
        p += 1
    prime[0], prime[1] = False, False
    for p in range(n + 1):
        if prime[p] == True: ans.append(p)
    return ans
    
#Build a try_comp function
#(needed for the Miller Rabin function)
def try_comp(a, d, n, s):
    if pow(a, d, n) == 1: return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1: return False
    return True
    
#Build a Miller Rabin function
def MillerRabin(n, prec):
    d, s = n - 1, 0
    ps = SoE(prec)
    maxes = [1373653, 25326001, 118670087467, 2152302898747]
    maxes.append(3474749660383)
    maxes.append(341550071728321)
    while not d % 2:
        d, s = d >> 1, s + 1
    for i in range(len(maxes)):
        x = i + 2
        if n < maxes[i]:
            if i == 2 and n == 3215031751: return False
            return not any(try_comp(a, d, n, s) for a in ps[:x])
    return not any(try_comp(a, d, n, s) for a in ps)

#Build the final isPrime function
def isPrime(n):
    if n < 10**4: return isPrime_dumb(n)
    else: return MillerRabin(n, len(str(n)))
    
#Build an isPrimeProof function
def isPrimeProof(n):
    sn = str(n)
    for char in range(len(sn)):
        for num in range(10):
            g = sn[:char] + str(num) + sn[char + 1::]
            if isPrime(int(g)): return False
    return True
    
#Build a suffix function
def buildSuffix(num):
    suffs = ['th', 'st', 'nd', 'rd']
    suff = suffs[0]
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        lastdigit = int(str(num)[-1])
        if lastdigit < len(suffs):
            suff = suffs[lastdigit]
    return suff

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    squbes = set()
    #These two were determined through trial and error
    ps = SoE(10**6)
    maxy = 10**12 / 4.3
  
    #Solve the problem
    for p in ps:
        for q in ps:
            if p == q: continue
            sqube = p**2 * q**3
            if sqube > maxy: break
            if sqube % 5 == 0 or sqube % 2 == 0:
                if str(lim) in str(sqube):
                    if isPrimeProof(sqube):
                        squbes.add(sqube)
                        
    squbes = list(squbes)
    squbes.sort()
    ans = str(squbes[lim - 1])
    s = buildSuffix(lim)
    lim = str(lim)

    #Print the results
    print('The ' + lim + s + ' prime-proof sqube containing ')
    print('the contiguous sub-string "' + lim + '" is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 200
solve(lim)
