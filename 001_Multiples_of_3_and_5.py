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
def inex(lim, mults):
    ans = 0
    for i in range(len(mults)):
        for j in co(mults, i + 1):
            ans += (-1)**i * SoM(lim, prod(list(j)))
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
def SumOfMults(lim, mults):
    #Declare variables
    start = time.time()
    strnums = ''
    
    #Solve the problem
    ans = str(inex(lim, mults))
            
    #Print the results
    print('The sum of all of the multiples of ')
    print(toString(mults) + ' below ' + str(lim) + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 1000
mults = {3, 5}
SumOfMults(lim, mults)

'''The SoM function runs in O(1) time, so the size of the limit is irrelevant. 

The inex function, on the other hand runs 2^(len(mults)) - 1 cycles, or O(2^(mults + 1)), 
where mults is the number of multiples we're solving for. As a result, regardless of the 
size of the limit, the SumOfMults function will be able to find the result in under 60 
seconds as long as the number of distinct multiples is around 23 or less, depending
on the speed of your machine.'''
