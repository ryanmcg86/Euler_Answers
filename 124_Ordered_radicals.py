'''The radical of n, rad(n), is the product of the distinct prime factors of n. 
For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), 
and sorting on n if the radical values are equal, we get:

Unsorted                    Sorted

n   rad(n)                  n   rad(n)    k
1   1                       1   1         1
2   2                       2   2         2
3   3                       4   2         3
4   2                       8   2         4
5   5                       3   3         5
6   6                       9   3         6
7   7                       5   5         7
8   2                       6   6         8
9   3                       7   7         9
10  10                      10  10        10

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
Link: https://projecteuler.net/problem=124'''

#Imports
import time

#Build a primeFactors function
def primeFactors(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n /= 2
    if n % 3 == 0:
        factors.append(3)
        while n % 3 == 0:
            n /= 3
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n /= i
        if n % (i + 2) == 0:
            factors.append(i + 2)
            while n % (i + 2) == 0:
                n /= (i + 2)
    if n > 2:
        factors.append(n)
    return factors

def rad(n):
    mult = 1
    factors = primeFactors(n)
    for i in range(0, len(factors)):
        mult *= factors[i]
    return mult
    
def E(k):
    return sorted(rads)[k - 1][1]


#Build a Solve function
def Solve(limit, k):
    start = time.time()
    
    rads = []
    for i in range(1, limit + 1):
        rads.append([rad(i), i])
        
    ans = str(E(k))

    #Print the results
    print 'With rad(n) sorted for 1 <= n <= ' + str(limit) + ', E(' + str(k) + ') = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 100000
k = 10000
Solve(limit)
