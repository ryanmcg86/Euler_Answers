'''The number, 1406357289, is a 0 to 9 pandigital number because it is made 
up of each of the digits 0 to 9 in some order, but it also has a rather 
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4  = 406 is divisible by 2
d3d4d5  = 063 is divisible by 3
d4d5d6  = 635 is divisible by 5
d5d6d7  = 357 is divisible by 7
d6d7d8  = 572 is divisible by 11
d7d8d9  = 728 is divisible by 13
d8d9d10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
Link: https://projecteuler.net/problem=43'''

#Imports
from itertools import permutations as p
import time

#Build a has-the-given-property function
def hasProperty(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        j = i + 3
        p = i - 1
        sub = int(str(num)[i:j])
        if sub % primes[p] != 0:
            return False
    return True

#Build a solve function
def solve(digits):
    #Declare variables
    start  = time.time()
    perms  = list(p(digits))
    total  = 0

    #Sum up the pandigitals that have the property
    for i in range(0, len(perms)):
        num = ''.join(str(digit) for digit in perms[i])
        if hasProperty(num):
            total += int(num)

    #Print the results
    print 'The sum of all 0 to 9 pandigital numbers with the given '
    print 'property is ' + str(total) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
solve(digits)
