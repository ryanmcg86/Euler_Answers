'''The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
Link: https://projecteuler.net/problem=12'''

#Imports
import time

#Build a function that finds the triangle
#number for n natural numbers
def tri(num):
    return num * (num + 1) / 2
    
#Build a function that returns all the divisors
#for a given input
def divisors(num):
    divs = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs.append(i)
            divs.append(num / i)
    divs.append(num)
    divs = sorted(divs)
    return list(set(divs))
    
#Build a function that returns the amount
#of divisors a given input has
def countdivs(num):
    return len(divisors(num))

#Build a function that solves the problem
def solve(num):
    start = time.time()
    i = 1
    while countdivs(tri(i)) <= num:
        i += 1
    
    print 'The value of the first triangle number to have over '
    print str(num) + ' divisors is ' + str(tri(i)) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Find the greatest product of four adjacent numbers in the same direction in the grid
num = 500
solve(num)
