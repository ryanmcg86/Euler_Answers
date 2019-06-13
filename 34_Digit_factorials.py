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
        #Rather than testing every number up to 9! * 7,
        #I only test every combination of digits 0-9 (repeats allowed)
        #for each length of number up to (and including) 7.
        #19437 < 2540160, and therefore runs much faster.
        for comb in cwr(facts, digits):
            num = ''
            sumfacts = 0
            for i in range(0, len(comb)):
                num += str(comb[i][0])
                sumfacts += comb[i][1]
            #Since we're not checking every number, I can only confirm
            #it's a match if I sort both numbers, and then check for equality.
            if sorted(str(sumfacts)) == sorted(num):
                total += sumfacts
                
    total = str(total)

    print 'The sum of all numbers which are equal to '
    print 'the sum of the factorial of their digits is ' + total + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program			
Solve()

'''As an aside, the amount of distinct combinations of the n = 10 digits (0-9), 
where we only have numbers of r length (so we're choosing r digits from the 0-9 pool, with repeats), 
can be calculated with the following formula:

(r + n - 1)! / r!(n - 1)!

For numbers of length 2 through 7, the following amount of combinations are created:
2: 55
3: 220
4: 715
5: 2002
6: 5005
7: 11440

We only have to go up to 7 digits, because the largest value an 8-digit number (99999999) can have its factorials sum 
up to is 2903040, meaning that all other possibilities will be less than that, and 8-digit numbers, by definition,
are ALL larger than that. This is only worsened as the number of digits increases, so it's impossible for any
numbers with more than 7 digits to have the sum of the factorials of their digits equal the original number.

The sum of all the combinations for numbers ranging in length from 2 digits to 7 digits is 19437, or

Σ i = 2, 7 for (10 + i - 1)! / 10!(i - 1)!
'''
