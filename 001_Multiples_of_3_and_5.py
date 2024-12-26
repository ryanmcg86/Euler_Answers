'''If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Link: https://projecteuler.net/problem=1'''

#Imports
import time
from math import prod, gcd
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

#Build a clean-Multiples function
def cleanMults(mults):
    divisors = set()
    for d in (1, -1):
        seen = 1
        #the list forwards, then the list backwards...
        for a in mults[::d]:
            if seen % a != 0: seen = a * seen // gcd(a, seen)
            else: divisors.add(a)
    return [a for a in mults if all(d == a or a % d != 0 for d in divisors)]
            
#Build a toString function
def toString(mults):
    lm = list(mults)
    if len(lm) == 1: return str(lm[0])
    s = 'or ' + str(lm[-1])
    for i in range(len(lm) - 2, -1, -1):
        s = str(lm[i]) + ', ' + s
    return s

#Sum of multiples (of 3 and 5) function
def SumOfMults(lim, mults):
    #Declare variables
    start = time.time()
    
    #Solve the problem
    ans, l, m = str(inex(lim, cleanMults(mults))), str(lim), toString(mults)
            
    #Print the results
    print('The sum of all of the multiples ')
    print('of ' + m + ' below ' + l + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 1000
mults = [3, 5]
SumOfMults(lim, mults)

'''The SoM function runs in O(1) time, so the size of the limit is irrelevant. 

The inex function, on the other hand, runs 2^(len(mults)) - 1 cycles, or O(2^n), 
where mults (or n) is the number of multiples we're solving for. As a result, 
regardless of the size of the limit, the SumOfMults function will be able to find 
the result in under 60 seconds as long as the number of distinct multiples is around 
23 or less, depending on the speed of your machine.

The cleanMults function deals with lists of multiples where 1 entry is a multiple of 
another. Example: [3, 6, 8] needs to become [3, 8], as the multiples throws off
the math of the inclusion-exclusion function. This runs in O(n) time, where n 
is the length of the list of multiples. This is a big improvement on O(n^2), 
which is what it would be if we compared every element in the given list of multiples 
to every other element in the given list of multiples.'''
