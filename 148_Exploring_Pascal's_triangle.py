'''We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   5  10   10  5   1
1   6  15  20  15   6   1
However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.
Link: https://projecteuler.net/problem=148'''

#Imports
import time
    
#Build a gauss function
def gauss(n):
    return n * (n + 1) / 2
    
#Build an f function
def f(n):
    if n <= 7:
        return gauss(n)
    ans = gauss(7)
    mod = 7
    while mod * 7 <= n:
        ans *= gauss(7)
        mod *= 7
    level = n / mod
    ans *= gauss(level)
    ans += (n / mod + 1) * f(n % mod)
    return ans

#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    
    #Solve the problem
    a = str(f(limit))
    l = str(limit)

    #Print the results
    print 'There are ' + a + ' entries below ' + l + ' not divisible by 7.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**9
solve(limit)
