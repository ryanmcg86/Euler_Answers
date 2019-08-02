'''Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 
1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, 
N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, 
there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, 
it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d  M(4, d)  N(4, d)  S(4, d)
0          2         13      67061
1          3          9      22275
2          3          1       2221
3          3         12      46214
4          3          2       8888
5          3          1       5557
6          3          1       6661
7          3          9      57863
8          3          1       8887
9          3          7      48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
Link: https://projecteuler.net/problem=111'''

#Imports
import time
from itertools import combinations as comb, product as prod

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

#Build a solve function
def solve(limit):
    #Declare variables
    start = time.time()
    numLen = limit
    primes = [[] for x in range(10)]
    
    #Solve the problem
    #(by building candidates and testing for primeness)
    for d in range(0, 10):
        if d > 0: m = numLen - 1
        else:     m = numLen - 2
        digits = [i for i in range(0, 10) if i != d]		#get all non-d digits
        while primes[d] == []:
            for x in comb(range(0, numLen), numLen - m):
                if d == 0 and 0 not in x: continue		#Skip if the number starts with 0
                num = [d for i in range(0, numLen)]
                for y in prod(digits, repeat = numLen - m):
                    if x[0] == 0 and y[0] == 0: continue
                    z = 0
                    for k in x:
                        num[k] = y[z]
                        z += 1
                    numInt = int(''.join(map(str, num)))
                    if isPrime(numInt):
                        primes[d].append(numInt)
            m -= 1
	
    ans = str(sum(sum(x) for x in primes))
    
    #Print the results
    print 'For d = 0 to 9, the sum of all S(' + str(limit) + ', d) is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10
solve(limit)
