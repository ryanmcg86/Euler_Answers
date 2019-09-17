'''Take the number 6 and multiply it by each of 1273 and 9854:

6 × 1273 = 7638
6 × 9854 = 59124

By concatenating these products we get the 1 to 9 pandigital 763859124. We will call 763859124 the 
"concatenated product of 6 and (1273,9854)". Notice too, that the concatenation of the input numbers, 
612739854, is also 1 to 9 pandigital.

The same can be done for 0 to 9 pandigital numbers.

What is the largest 0 to 9 pandigital 10-digit concatenated product of an integer with two or more other integers, 
such that the concatenation of the input numbers is also a 0 to 9 pandigital 10-digit number?
Link: https://projecteuler.net/problem=170'''

#Imports
import time
from itertools import permutations as p

#Build a divisors function
def divisors(n):
    divs = [1, n]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n / i)
    return list(sorted(set(divs)))
    
#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x
   
#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    digits = [str(i) for i in reversed(range(10))]
    ans = 0
    found = False
    
    #Solve the problem
    for perm in p(digits):
        if found: break
        n = int(''.join(perm))
        for k in range(1, 10):
            if found: break
            t = 10**k
            c1 = n / t
            c2 = n % t
            if c1 == 0 or c2 == 0: continue
            g = gcd(c1, c2)
            if g == 1: continue
            for d in divisors(g):
                d1 = str(c1 / d)
                d2 = str(c2 / d)
                d = str(d)
                if sorted(''.join((d1, d2, d)), reverse = True) == digits:
                    found = True
                    ans = n
                    break
        
    ans = str(ans)

    #Print the results
	print 'The largest 0 to 9 pandigital 10-digit concatenated '
	print 'product of an integer with two or more other integers, '
	print 'such that the concatenation of the input numbers is ' 
	print 'also a 0 to 9 pandigital 10-digit number, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
