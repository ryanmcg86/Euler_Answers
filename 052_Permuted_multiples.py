'''It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
Link: https://projecteuler.net/problem=52'''

#Imports
import time

#Build a hasProperty function
def hasProperty(n):
    num = sorted(str(n))
    for i in range(2, 7):
        if sorted(str(n * i)) != num:
            return False
    return True

#Build a solve function
def solve():
    #Define variables
    start = time.time()
    ans = 1
	
    #Solve the problem
    while hasProperty(ans) == False:
        ans += 1

    #Print the results
    print 'The smallest positive integer, x, such that 2x, 3x, '
    print '4x, 5x, and 6x, contain the same digits, is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
