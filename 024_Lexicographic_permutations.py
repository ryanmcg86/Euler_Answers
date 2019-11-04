'''A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
Link: https://projecteuler.net/problem=24'''

#Imports
import time

#Build a factorial function
def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

#Build a suffix function
def buildSuffix(num):
    suff = 'th'
    begin = len(str(num)) - 2
    end = begin + 1
    suffixes = [[1, 'st'], [2, 'nd'], [3, 'rd']]
    if str(num)[begin:end] != '1':
        for i in range(0, len(suffixes)):
            if int(str(num)[-1]) == suffixes[i][0]
                suff = suffixes[i][1]
    return suff

#Build a perm function
def perm(n, s):
    if len(s) == 1: return s
    q, r = divmod(n, fact(len(s) - 1))
    return s[q] + perm(r, s[:q] + s[q + 1:])

#Build a lexigraphic permutation function
#that returns the nth lexigraphic permutation
#of a given input of numbers 
def lexiPermutation(digits, permCount):
    start     = time.time()
    num       = perm(permCount - 1, digits)
    suff      = buildSuffix(permCount)
    permCount = str(permCount) + suff
    
    print 'The ' + permCount + ' lexicographic permutation of the given digits is ' + str(num) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
digits = '0123456789'
permCount = 1000000
lexiPermutation(digits, permCount)
