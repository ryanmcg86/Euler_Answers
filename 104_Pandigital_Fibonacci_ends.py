'''The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for 
which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). 
And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
Link: https://projecteuler.net/problem=104'''

#Imports
import time
from itertools import permutations as p

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
def solve():
    #Define variables
    start = time.time()
    a1    = 1
    b1    = 1
    a2    = 1
    b2    = 1
    ans   = 1
    pandigitals = set()
    for i in p('123456789', 9):
        pandigitals.add(int(''.join(str(j) for j in i)))
        
    #Solve the problem
    while True:
        ans += 1
        a1, b1 = b1, a1 + b1
        a2, b2 = b2, a2 + b2
        a1 %= 10**9
        while a2 > 10**18:
            a2 /= 10
            b2 /= 10
        if a1 in pandigitals:
            if int(str(a2)[:9]) in pandigitals:
                break
                
    ans = str(ans) + buildSuffix(ans)
    
    #Print the results
    print 'The ' + ans + ' Fibonacci number is the first one where both the '
    print 'first nine digits and the last nine digits are pandigital.'    
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
