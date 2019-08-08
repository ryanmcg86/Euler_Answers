'''The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. 
Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
Link: https://projecteuler.net/problem=119'''

#Imports
import time

def buildSuffix(num):
    suffs = ['th', 'st', 'nd', 'rd']
    suff = suffs[0]
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        lastdigit = int(str(num)[-1])
        if lastdigit < len(suffs):
            suff = suffs[lastdigit]
    return suff

#Build a solve function
def solve(n):
    #Declare variables
    start = time.time()
    answers = set()
    exp = 1
    
    #Solve the problem
    while len(answers) <= n:
        exp += 1
        for base in range(2, n * 50):
            number = base**exp
            dSum = sum([int(digit) for digit in str(number)])
            if dSum == base:
                answers.add(number)
        
    ans = str(sorted(answers)[n - 1])
    num = str(n) + buildSuffix(n)
                
    #Print the results
    print 'The ' + num + ' number in the sequence of numbers '
    print 'where the sum of N\'s digits can equal N when '
    print 'raised to some power, is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 30
solve(n)
