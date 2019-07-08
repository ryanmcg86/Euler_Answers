'''The 5-digit number, 16807=75, is also a fifth power. Similarly, 
the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
Link: https://projecteuler.net/problem=63'''

#Imports
import time

#Build a solve function
def solve():
    #Define variables
    start = time.time()
    count = 0

    #Solve the problem
    for i in range(1, 10):
        for n in range(1, 22):
            if len(str(i**n)) == n:
                count += 1

    #Print the results
    print str(count) + 'n-digit positive integers exist which are also an nth power.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()

'''Note: 1 <= i < 10, because if i >= 10, the amount of digits in i**n will always be greater than
n itself. The smallest possible example shows this: if i = 10 and n = 1, 10**1 = 10. Since 10 has a length
of 2, and n is only 1, this shows that i's upper bound is 9.

Note: 1 <= n < 22, because len(str(9**21)) and len(str(9**22)), where 9 is the max i value, both have a length of 21. 
As n increases while i is at its max(9), len(str(9**n)) grows more slowly than n itself. Therefore the upper
bound of n is 21.'''
