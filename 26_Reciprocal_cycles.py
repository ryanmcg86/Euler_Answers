'''A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
Link: https://projecteuler.net/problem=26'''

#Imports
import time
    
#Build a function that returns the length
#of a repeating cycle for a given denominator
# in a unit-fraction
def cycle_length(denom):
	cycle = []
	remains = (10**len(str(denom))) % denom
	while remains not in cycle and remains != 0:
		cycle.append(remains)
		remains = (remains * 10) % denom
	if remains == 0:
		return 0
	else:
		return len(cycle) - cycle.index(remains)

#Build a function that returns the denominator
#with the longest cycle of a unit fraction
#up to the inputted number
def findDenom(num):
    start = time.time()
    
    maxlen = 0
    
    for denom in range(num - 1, 2, -1):
        if cycle_length(denom) == (denom - 1):
            maxlen = denom
            break
        
    print 'The value of d < ' + str(num) + ' for which 1/d contains the longest '
    print 'recurring cycle in its decimal fraction part is ' + str(maxlen) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 1000
findDenom(num)
