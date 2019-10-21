'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Link: https://projecteuler.net/problem=5'''

#Imports
import time
from functools import reduce

#Lowest Common Multiple function
def lcm(a, b):
    a1, b1 = a, b
    while b:
        a, b = b, a % b
    return a1 * b1 // a

#lcm function for more than 2 numbers
def lcms(n):
    return reduce(lcm, [i for i in range(1, n + 1)])

#Run function
def run(n):
    #Declare variables
    start = time.time()
    
    #Solve the problem
    ans = str(lcms(n))
            
    #Print the results
    print('The smallest positive number that is evenly divisible ')
    print('by all of the numbers from 1 to ' + str(n) + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Run the program
n = 20
run(n)
