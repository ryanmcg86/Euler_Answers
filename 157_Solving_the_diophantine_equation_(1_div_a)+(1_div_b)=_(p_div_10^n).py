'''Consider the diophantine equation 1/a+1/b= p/10n with a, b, p, n positive integers and a ≤ b.
For n=1 this equation has 20 solutions that are listed below:

(1 /  1) + (1 /   1) = (20 / 10)
(1 /  1) + (1 /   2) = (15 / 10)
(1 /  1) + (1 /   5) = (12 / 10)
(1 /  1) + (1 /  10) = (11 / 10)
(1 /  2) + (1 /   2) = (10 / 10)
(1 /  2) + (1 /   5) = ( 7 / 10)
(1 /  2) + (1 /  10) = ( 6 / 10)
(1 /  3) + (1 /   6) = ( 5 / 10)
(1 /  3) + (1 /  15) = ( 4 / 10)
(1 /  4) + (1 /   4) = ( 5 / 10)
(1 /  4) + (1 /  20) = ( 3 / 10)
(1 /  5) + (1 /   5) = ( 4 / 10)
(1 /  5) + (1 /  10) = ( 3 / 10)
(1 /  6) + (1 /  30) = ( 2 / 10)
(1 / 10) + (1 /  10) = ( 2 / 10)
(1 / 11) + (1 / 110) = ( 1 / 10)
(1 / 12) + (1 /  60) = ( 1 / 10)
(1 / 14) + (1 /  35) = ( 1 / 10)
(1 / 15) + (1 /  30) = ( 1 / 10)
(1 / 20) + (1 /  20) = ( 1 / 10)
How many solutions has this equation for 1 ≤ n ≤ 9?
Link: https://projecteuler.net/problem=157'''

#Imports
import time

#Build a tau function
#Returns the total number of divisors of input n
def tau(n):
    count = 0
    sqrt = int(n**0.5)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            count += 1
    count *= 2
    if sqrt * sqrt == n:
        count -= 1
    return count
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = 0
    
    #Solve the problem
    for n in range(1, limit + 1):
        for k1 in range(1, n + 1):
            for l1 in range(1, n + 1):
                a = (n - k1 + 1)
                b = (n - l1 + 1)
                c = tau(2**k1 + 5**l1)
                ans += a * b * c
        for k1 in range(n + 1):
            for l1 in range(n + 1):
                a = 1 + 2**k1 * 5**l1
                if k1 != 0 and l1 != 0:
                    b = (n - k1 + 1)
                    c = (n - l1 + 1)
                    ans += tau(a) * b * c
                else:
                    b = 2**(n - k1)
                    c = 5**(n - l1)
                    ans += tau(a * b * c)
    
    #Print the results
    print 'For the given diophantine equation, '
    print '(1 / a) + (1 / b) = (p / 10**n), '
    print 'there are ' + str(ans) + ' solutions when n '
    print 'is in range 1 <= n <= ' + str(limit) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 9
solve(limit)
