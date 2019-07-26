'''Comparing two numbers written in index form like 211 and 37 is not difficult, 
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, 
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing 
one thousand lines with a base/exponent pair on each line, determine which line number has 
the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
Link: https://projecteuler.net/project/resources/p099_base_exp.txt
Link: https://projecteuler.net/problem=99'''

#Imports
import time
import math

#Build a solve function
def solve(filename):
    #Define variables
    start = time.time()
    maxnum = 0
    maxb = 0
    maxe = 0
    linenum = 0
    f = open(filename, 'r')
    nums = f.read().split('\n')
    numbers = []
    
    #Solve the problem
    for i in range(0, len(nums)):
        n1 = nums[i][0:nums[i].find(',')]
        n2 = nums[i][nums[i].find(',') + 1:]
        numbers.append([int(n1), int(n2)])

    for i in range(0, len(numbers)):
        base = numbers[i][0]
        exp = numbers[i][1]
        log = exp * math.log(base, 2)
        if log > maxnum:
            maxnum = log
            maxb = base
            maxe = exp
            linenum = i + 1

    num = str(maxb) + '^' + str(maxe)
    linenum = str(linenum)
    
    #Print the results
    print 'The line number with the greatest '
    print 'numerical value, ' + num + ', is ' + linenum + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
filename = 'base_exp.txt'
solve(filename)
