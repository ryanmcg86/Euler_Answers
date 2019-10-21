'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
Link: https://projecteuler.net/problem=15'''

#Imports
import time

#Build a factorial function
def fact(num):
    ans = 1
    for i in range(num, 1, -1):
        ans *= i
    return ans
    
#Build an nCr function
def nCr(n, r):
    return int(fact(n) / (fact(r) * fact(n - r)))

#Solution function
def solve(r, s):
    #Define variables
    start = time.time()
    n = r + s
    
    #Solve the problem
    ans = str(nCr(n, r))
    grid = str(r) + 'x' + str(s) + ' grid'
    
    #Print the reuslts
    print('When only being able to move to the right and down, ')
    print('there are ' + ans + ' total routes through a ' + grid + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
r = 20
s = 20
solve(r, s)
