'''A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
Link: https://projecteuler.net/problem=24'''

#Imports
import time
from itertools import permutations

#Build a suffix function
def buildSuffix(num):
    suff = 'th'
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        if   int(str(num)[-1]) == 1:
            suff = 'st'
        elif int(str(num)[-1]) == 2:
            suff = 'nd'
        elif int(str(num)[-1]) == 3:
            suff = 'rd'
    return suff

#Build a lexigraphic permutation function
#that returns the nth lexigraphic permutation
#of a given input of numbers 
def lexiPermutation(digits, permCount):
    start = time.time()
    
    perm = permutations(digits)
    lexiperm = 0
    counter = 0
    for i in list(perm):
        counter += 1
        if counter == permCount:
            num = ''
            for digit in i:
                num += str(digit)
            lexiperm = int(num)
     
    suff = buildSuffix(permCount)
    num = str(permCount) + suff
    
    print 'The ' + num + ' lexicographic permutation of the given digits is ' + str(lexiperm) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permCount = 1000000
lexiPermutation(digits, permCount)
