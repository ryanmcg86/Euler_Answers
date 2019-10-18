'''For some positive integers k, there exists an integer partition of the form   4^t = 2^t + k,
where 4^t, 2^t, and k are all positive integers and t is a real number.

The first two such partitions are 4^1 = 2^1 + 2 and 4^1.5849625... = 2^1.5849625... + 6.

Partitions where t is also an integer are called perfect.
For any m ≥ 1 let P(m) be the proportion of such partitions that are perfect with k ≤ m.
Thus P(6) = 1/2.

In the following table are listed some values of P(m)

   P(5) = 1 / 1
   P(10) = 1 / 2
   P(15) = 2 / 3
   P(20) = 1 / 2
   P(25) = 1 / 2
   P(30) = 2 / 5
   ...
   P(180) = 1 / 4
   P(185) = 3 / 13

Find the smallest m for which P(m) < 1 / 12345
Link: https://projecteuler.net/problem=207'''

#Imports
import time
import math

#Build a is power of # function
def isPowOf(n, p):
    top = math.ceil(math.log(n, p))
    bottom = math.floor(math.log(n, p))
    return top == bottom

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    pm, perf, n, ans = 0.0, 1, 2, 0

    #Solve the problem
    while True:
        pm = perf / n
        if pm < lim[0] / float(lim[1]):
            ans = str(n * (n + 1))
            break
        n += 1
        if isPowOf(n, 2):
            perf += 1
            
    frac = str(lim[0]) + '/' + str(lim[1]) 

    #Print the results
    print('The smallest m for which P(m) < ' + frac + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = [1, 12345]
solve(lim)
