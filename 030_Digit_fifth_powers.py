'''Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
Link: https://projecteuler.net/problem=30'''

#Imports
import time
from itertools import combinations_with_replacement as cwr

#Build a suffix function
def buildSuffix(num):
    suff  = 'th'
    begin = len(str(num)) - 2
    end   = begin + 1
    suffixes = [[1, 'st'], [2, 'nd'], [3, 'rd']]
    if str(num)[begin:end] != '1':
        for i in range(0, len(suffixes)):
            if int(str(num)[-1]) == suffixes[i][0]:
                   suff = suffixes[i][1]
    return suff

#Build a sum of power digits for exponent function
def sopdfe(ex):
    s, p = 0, {str(i):i**ex for i in range(10)}
    if ex >= 5: ex += 1
    for cx in cwr('0123456789', ex):
        t  = sum(p[x] for x in cx)
        sd = sum(p[x] for x in str(t))
        if t == sd and t > 9: s += t
    return (s if s > 0 else "NONE")   

#Build a answer function
def answer(power):
    start, ps = time.time(), str(sopdfe(power))
    p = str(power) + buildSuffix(power) + ' powers of their digits'

    if ps == 'NONE':
        print('There are no numbers that can be written ')
        print('as the sum of ' + p + '.')
    else:
        print('The sum of all the numbers that can be written ') 
        print('as the sum of ' + p + ' is ' + ps + '.')

    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Run the program
power = 5
answer(power)
