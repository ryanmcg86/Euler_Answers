'''If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Link: https://projecteuler.net/problem=1'''

#Imports
import time
from math import prod
from itertools import combinations as co

#Build a Sum of Multiples function
def SoM(lim, mul):
    n = (lim - 1) // mul
    return (n * (n + 1) * mul) // 2

#Build an inclusion-exclusion function
def inex(n, mults):
    num, ans = -1, 0
    for i in range(1, len(mults) + 1):
        for j in co(mults, i):
            ans += num**(i + 1) * SoM(n, prod(list(j)))
    return ans

#Build a toString function
def toString(mults):
    if len(mults) == 1: return str(mults[0])
    strnums = ''
    for i in range(len(mults)):
        if i != len(mults) - 1:
            strnums += str(list(mults)[i]) + ', '
        else:
            strnums = strnums[:-2]
            strnums += ' and ' + str(list(mults)[i])
    return strnums

#Sum of multiples (of 3 and 5) function
def SumOfMults(n, mults):
    #Declare variables
    start = time.time()
    strnums = ''
    
    #Solve the problem
    ans = str(inex(n, mults))
            
    #Print the results
    print('The sum of all of the multiples of ')
    print(toString(mults) + ' below ' + str(n) + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
n = 1000
mults = {3, 5}
SumOfMults(n, mults)
