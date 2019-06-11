'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals (21, 7, 1, 3, 13, 17, 4, 9, and 25) is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
Link: https://projecteuler.net/problem=28'''

#Imports
import time

#Build a spiralSum function
def spiralSum(num):
	total = 1
	for i in range(3, num + 1, 2):
		side = (i - 1)
		for j in range(0, 4):
			total += i**2 - (j * side)
	return total

#Build a answer function
def answer(num):
    start = time.time()
    
    ans = spiralSum(num)
    grid = str(num) + ' by ' + str(num)
    
    print 'The sum of the numbers on the diagonals in a ' + grid + ' spiral is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
num = 1001
answer(num)
