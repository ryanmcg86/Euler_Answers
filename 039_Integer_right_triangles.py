'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
Link: https://projecteuler.net/problem=39'''

#Imports
import time

#Build a Solve function
def solve(n):
    #Declare variables
    start, p = time.time(), [0] * (n + 1)
    
    #Solve the problem
    for a in range(1, n // 3 + 1):
        for b in range(a + 1, n // 2):
            c = int((a**2 + b**2)**0.5)
            if a**2 + b**2 == c**2 and a + b + c <= n:
                p[a + b + c] += 1
    
    #Print the results
    print('The value for which p <= ' + str(n) + ' ')
    print('is maximized is ' + str(p.index(max(p))) + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Run the program
num = 1000
solve(num)
