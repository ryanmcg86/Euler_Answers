'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
Link: https://projecteuler.net/problem=34'''

#Imports
from itertools import combinations_with_replacement as cwr
import time

#Build a factorial function
def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

#Build a Solve function
def Solve():
    start = time.time()

    facts = []
    total = 0
    
    for i in range(0, 10):
        facts.append([i, fact(i)])
        
    for digits in range(2, 8):
        for comb in cwr(facts, digits):
            num = ''
            sumfacts = 0
            for i in range(0, len(comb)):
                num += str(comb[i][0])
                sumfacts += comb[i][1]
            if sorted(str(sumfacts)) == sorted(num):
                total += sumfacts
                
    total = str(total)

    print 'The sum of all numbers which are equal to '
    print 'the sum of the factorial of their digits is ' + total + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program			
Solve()
