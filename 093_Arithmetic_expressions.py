'''By using each of the digits from the set, {1, 2, 3, 4}, exactly once, 
and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, 
it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, 
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 
1 to n, can be obtained, giving your answer as a string: abcd.
Link: https://projecteuler.net/problem=93'''

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
