'''The binomial coefficients (nk) can be arranged in triangular form, Pascal's triangle, like this:

1	
1		1	
1		2		1	
1		3		3		1	
1		4		6		4		1	
1		5		10		10		5		1	
1		6		15		20		15		6		1	
1		7		21		35		35		21		7		1
.........
It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers: 
1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n. 
Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree. 
The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.
Link: https://projecteuler.net/problem=203'''

#Imports
import time

#Build a factorial function
def fact(n):
    return fact(n - 1) * n if n > 1 else 1
  
#Build a Binomial Coefficient function
def nCr(n, r):
    return int(fact(n) / (fact(r) - fact(n - r)))
    
#Build a Pascal function
def Pascal(n):
    ans = set()
    for i in range(n):
        for j in range(i + 1):
            ans.add(nCr(i, j))
    return sorted(list(ans))
    
#Build a Sieve of Eratosthenes function
def SoE(n):
    prime = [False, False] + [True for i in range(n - 1)]
    ans, p = [], 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(n + 1):
        if prime[p]: ans.append(p)
    return ans
    
#Build an is Square-free function
def isSqFree(n, ps2):
    for p2 in ps2:
        if p2 > n: break
        if n % p2 == 0: return False
    return True

#Build a Solve function
def solve(rows):
    #Define variables
    start = time.time()
    dist = Pascal(rows)
    ps = SoE(rows) #Any prime dividing C(n,k) is ≤ n, so you need only the primes up to rows.
    ps2 = [i**2 for i in ps]
    sqfree = 0
    
    #Solve the problem
    for i in dist:
        if isSqFree(i, ps2):
            sqfree += i
            
    ans = str(sqfree)
    rows = str(rows)

    #Print the results
    print('The sum of the distinct squarefree numbers in the ')
    print('first ' + rows + ' rows of Pascals triangle is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
rows = 51
solve(rows)
