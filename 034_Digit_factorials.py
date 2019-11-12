'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
Link: https://projecteuler.net/problem=34'''

#Imports
import time
from itertools import combinations_with_replacement as cwr

def fact(n):
    return fact(n - 1) * n if n > 1 else 1

#Build a solve function
def solve():
    #Declare variables
    start = time.time()
    facts, ans = [[i, fact(i)] for i in range(10)], 0
    
    #Solve the problem    
    for digits in range(2, 8):
        for comb in list(cwr(facts, digits)):                        #Note 1
            num = ''.join(str(i[0]) for i in comb)
            sumfacts = sum(i[1] for i in comb)
            if sorted(str(sumfacts)) == sorted(num): ans += sumfacts #Note 2

    #Print the results
    print 'The sum of all numbers which are equal to the '
    print 'sum of the factorial of their digits is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program			
solve()

#Note 1: Rather than testing every number up to 9! * 7, I only test every combination of digits 0-9 (repeats allowed)
#for each length of number up to (and including) 7. 19437 < 2540160, and therefore runs much faster.

#Note 2: Since we're not checking every number, I can only confirm it's a match if I sort both numbers, and then check for equality.

'''As an aside, the amount of distinct combinations of the n = 10 digits (0-9), 
where we only have numbers of r length (so we're choosing r digits from the 0-9 pool, with repeats), 
can be calculated with the following formula:

(n + r - 1)! / r!(n - 1)!

For numbers of length 2 through 7, the following amount of combinations are created:
2: 55
3: 220
4: 715
5: 2002
6: 5005
7: 11440

We only have to go up to 7 digits, because the largest value an 8-digit number (99999999) has its factorials sum 
up to is 2903040, meaning that all other possibilities will be less than that, and 8-digit numbers, by definition,
are ALL larger than that. This is only worsened as the number of digits increases, so it's impossible for any
numbers with more than 7 digits to have the sum of the factorials of their digits equal the original number.

The sum of all the combinations for numbers ranging in length from 2 digits to 7 digits is 19437, or

Σ i = 2, 7 for (10 + i - 1)! / i!(10 - 1)!

or, in python:

def fact(n): return fact(n - 1) * n if n > 1 else 1
def comb(n, r): return fact(n + r - 1) // (fact(r) * fact(n - 1))
print(sum(comb(10, r) for r in range(2, 8)))
'''
