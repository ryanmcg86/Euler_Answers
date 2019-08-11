'''The radical of n, rad(n), is the product of distinct prime factors of n. 
For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.
Link: https://projecteuler.net/problem=127'''

#Imports
import time

#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x

#Build a Solve function
def Solve(limit):
    #Define variables
    start = time.time()
    ans = 0
    rads = [0] + [1] * (limit - 1)
	
    #Build a rad sieve
    for i in range(2, len(rads)):
        if rads[i] == 1:
            for j in range(i, len(rads), i):
                rads[j] *= i
    sortedRads = sorted((rad, n) for (n, rad) in enumerate(rads))
    sortedRads = sortedRads[1:]
    
    #Solve the problem
    for c in range(2, limit):
        for (rad, a) in sortedRads:
            rad *= rads[c]
            if rad >= c:
                break
            b = c - a
            if a < b and rad * rads[b] < c and gcd(a, b) == 1:
                ans += c

    ans = str(ans)
    limit = str(limit)
  
    #Print the results
    print 'The sum of all c\'s in abc-hits under ' + limit + ' is '  + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 120000
Solve(limit)
