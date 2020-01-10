'''2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
Link: https://projecteuler.net/problem=16'''

#Imports
import time

#Solution function
def solve(base, exp):
    start = time.time()
    ans = str(sum(int(i) for i in str(base**exp)))
    num = str(base) + '^' + str(exp)
    
    print 'The sum of the digits of the number ' + num + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
base = 2
exp = 1000
solve(base, exp)
