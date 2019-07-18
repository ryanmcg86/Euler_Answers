'''The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
Link: https://projecteuler.net/problem=60'''

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
    
#Build a build_sieve function
def build_sieve(n):
    if n < 2:
        return []
    if n < 3:
        return [2]
    ps = [2, 3]
    i = 5
    while i <= n:
        if isPrime(i):
            ps.append(i)
        if i + 2 > n:
            break
        if isPrime(i + 2):
            ps.append(i + 2)
        i += 6
    return ps
    
#Build a combine-check function
def comb(a, b):
    len_a = math.floor(math.log10(a)) + 1
    len_b = math.floor(math.log10(b)) + 1
    p1 = int(a*(10**len_b) + b)
    p2 = int(b*(10**len_a) + a)
    return isPrime(p1) and isPrime(p2)
    
#Build a getAnswer function
def getAnswer(ps): 
    for a in range(0, len(ps) - 4):
        for b in range(a + 1, len(ps) - 3):
            c1 = comb(ps[a], ps[b])
            if c1:
                for c in range(b + 1, len(ps) - 2):
                    c2 = comb(ps[a], ps[c])
                    c3 = comb(ps[b], ps[c])
                    if c2 and c3:
                        for d in range(c + 1, len(ps) - 1):
                            c4 = comb(ps[a], ps[d])
                            c5 = comb(ps[b], ps[d])
                            c6 = comb(ps[c], ps[d])
                            if c4 and c5 and c6:
                                for e in range(d + 1, len(ps)):
                                    c7  = comb(ps[a], ps[e])
                                    c8  = comb(ps[b], ps[e])
                                    c9  = comb(ps[c], ps[e])
                                    c10 = comb(ps[d], ps[e])
                                    if c7 and c8 and c9 and c10:
                                        return ps[a] + ps[b] + ps[c] + ps[d] + ps[e]

#Build a solve function
def solve(file):
    #Define variables
    start = time.time()
    ps = build_sieve(10000)

    #Solve the problem
    ans = getAnswer(ps)

    #Print the results
    print 'The lowest sum for a set of five primes for which any two primes '
    print 'concatenate to produce another prime is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
