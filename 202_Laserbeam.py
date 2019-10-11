'''Three mirrors are arranged in the shape of an equilateral triangle, with their reflective surfaces pointing inwards. 
There is an infinitesimal gap at each vertex of the triangle through which a laser beam may pass.

Label the vertices A, B and C. There are 2 ways in which a laser beam may enter vertex C, bounce off 11 surfaces, 
then exit through the same vertex: one way is shown below; the other is the reverse of that.

There are 80840 ways in which a laser beam may enter vertex C, bounce off 1000001 surfaces, then exit through the same vertex.

In how many ways can a laser beam enter at vertex C, bounce off 12017639147 surfaces, then exit through the same vertex?
Link: https://projecteuler.net/problem=202'''

#Imports
import time
import math

#Build a Jacobsthal numbers function
def b(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
    return dp[n]

#Build an n function
def n(lim):
    return int((lim + 3) / 2)
    
#Build a factors function
def factors(n):
    factors = []
    for i in range(2, 4):
        while n % i == 0:
            factors.append(i)
            n /= i
    for i in range(5, int(n**0.5) + 1, 6):
        plus2 = [i, i + 2]
        for j in plus2:
            while n % j == 0:
                factors.append(j)
                n /= j
    if n > 2:
        factors.append(n)
    return list(set(factors))
    
#Build a factor count function
def factCount(num):
    return len(factors(num))
    
#Build a phi function
def phi(n):
    facts = factors(n)
    ans = n
    for i in facts:
        ans *= (1 - 1 / float(i))
    return int(ans)
    
#Build an a function
def a(lim):
    one = math.ceil((phi(n(lim)) + 1 / 3)
    exp = factCount(n(lim))
    two = (-1)**exp * b(exp)
    return int(one + two)

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
  
    #Solve the problem
    ans, lim = str(a(lim)), str(lim)

    #Print the results
    print('A laser beam can enter at vertex C, ')
    print('bounce off ' + lim + ' surfaces, then ')
    print('exit through the same vertex ' + ans + ' ways.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 12017639147
solve(lim)
