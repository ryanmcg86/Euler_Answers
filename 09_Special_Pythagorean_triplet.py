'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
Link: https://projecteuler.net/problem=9'''

#Imports
import time

#Build a is-pythagorean function
def isPythag(a, b, c):
    return a**2 + b**2 == c**2

#Build a findProd function
def findProd(num):
    start = time.time()
    triplet = []
    for a in range(1, num / 3):
        b = a + 1
        c = num - a - b
        while a < b and b < c:
            if isPythag(a, b, c):
                triplet = [a, b, c]
                break
            b += 1
            c = num - a - b
    a, b, c = triplet[0], triplet[1], triplet[2]
    prod = str(a * b * c)
    a, b, c = str(a), str(b), str(c)
    
    print 'The Pythagorean triplet for which a + b + c = ' + str(num) + ' is ' + a + ', ' + b + ', and ' + c + '.'
    print 'The product of ' + str(a) + ' * ' + str(b) + ' * ' + str(c) + ' is ' + prod + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Find the product of the Pythagorean triplet for which a + b + c = 1000
num = 1000
findProd(num)
