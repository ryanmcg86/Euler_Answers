'''There are some prime values, p, for which there exists a positive integer, n, 
such that the expression n^3 + n^2*p is a perfect cube.

For example, when p = 19, 8^3 + 8^2 × 19 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, 
and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
Link: https://projecteuler.net/problem=131'''

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
    
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    pmax = 0
    p = (pmax + 1)**3 - pmax**3
    while p < limit:
        pmax += 1
        p = (pmax + 1)**3 - pmax**3
    ans = 0
    
    #Solve the problem
    for i in range(1, pmax):
        if isPrime((i + 1)**3 - i**3):
            ans += 1
        
    #Print the results
    print 'The number of primes below ' + str(limit)
    print 'with this remarkable property is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**6
solve(limit)

'''
Given that n^3 + n^2 * p = k^3, where k is a perfect cube and p is a prime, 
we can make the following simplifications:

n^3 * (p/n + 1) = k^3

n^3 * ((n + p) / n) = k^3

n * ((n + p) / n)**(1/3) = k

n * (n + p)**(1/3) / n**(1/3) = k

Therefore, k is only an integer when (n + p) and n are both perfect cubes.

Lets say variable x^3 = n and y^3 = p + n, we can say that p = y^3 - x^3.

If we use the differences of cubes rule, we get:

p = (y - x) * (y^2 + y * x + x^2)

For posterities sake, lets confirm this rule by foiling:

(y - x) * (y^2 + y * x + x^2)

(y^3) + (y^2 * x) + (y * x^2) - (x * y^2) - (x^2 * y) - (x^3)

If we regroup so we better see what gets cancelled:

(y^3) + (y^2 * x) - (y^2 * x) + (y * x^2) - (y * x^2) - x^3

and finally, after simplifying we get:

y^3 - x^3

Since we now know that p = (y - x) * (y^2 + y * x + x^2), we know that p is divisible
by (y - x). Since p is prime though, this is only possible if y - x = 1. Because of this, 
we know that p is the difference of 2 consecutive cubes. Therefore, all we need to do 
to solve this problem is check whether (i + 1)^3 - i^3 is prime for all i values where the 
result is less than our limit. To find the limit for i values to check, we use a while loop
to find the largest value that is under our limit. In our case, our limit being 1000000 makes
out max value to check 577.
'''
