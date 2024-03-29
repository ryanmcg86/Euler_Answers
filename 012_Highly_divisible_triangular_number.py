'''The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
Link: https://projecteuler.net/problem=12'''

#Imports
import time

#Build a function that finds the triangle
#number for n natural numbers
def tri(n):
    return n * (n + 1) // 2
    
#Build a function that returns the amount
#of divisors a given input has
def tau(n):
    exps, ans = [], 1
    for i in range(2, 4):
        if n % i == 0: exps.append(0)
        while n % i == 0:
            exps[-1] += 1
            n /= i
    for i in range(5, int(n**0.5) + 1, 6):
        plus2 = [i, i + 2]
        for j in plus2:
            if n % j == 0: exps.append(0)
            while n % j == 0:
                exps[-1] += 1
                n /= j
        if n == 1: break
    if n > 2: exps.append(1)    
    for i in exps: ans *= (i + 1)
    return ans

#Build a function that solves the problem
def solve(n):
    #Define variables
    s, i = time.time(), 1
    ans = tri(i)
    
    #Solve the problem
    while tau(ans) <= n:
        i += 1
        ans = tri(i)
      
    ans, n = str(ans), str(n)
    
    #Print the results
    print('The value of the first triangle number ')
    print('to have over ' + n + ' divisors is ' + ans + '.')
    print('This took ' + str(time.time() - s) + ' seconds to calculate.')
    
#Find the greatest product of four adjacent numbers in the same direction in the grid
n = 500
solve(n)
