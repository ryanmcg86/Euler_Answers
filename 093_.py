'''A number chain is created by continuously adding the square of the 
digits in a number to form a new number until it has been seen before.
For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
Link: https://projecteuler.net/problem=92'''

#Imports
import time
from itertools import combinations as c, permutations as p, count as co, product as pr
import operator as o

#Build a length function
def length(digits):
    outputs = set()
    ops = [o.add, o.sub, o.mul, o.truediv]
    for a, b, c, d in p(digits):
        for op1, op2, op3 in pr(ops, repeat = 3):
            outputs.update([
                op1(op2(op3(a, b), c), d), 
                op1(op2(a, b), op3(c, d))
            ])
    return next(i for i in co(1) if i not in outputs) - 1

#Build a solve function
def solve():
    #Define variables
    start = time.time()
    ans = ''

    #Solve the problem
    nums = max(c(range(1, 10), 4), key = length)
    for i in nums:
        ans += str(i)
    
    #Print the results
    print 'The string that represents the concatenation of the 4 single '
    print 'digit numbers where a < b < c < d, for which the longest set of '
    print 'consecutive positive integers, 1 to n, can be obtained, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
solve()
