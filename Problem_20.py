'''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
Link: https://projecteuler.net/problem=20'''

#Imports
import time
import datetime

#Build a sum-of-factorial-digits function
def sumOfFactorialDigits(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= 1
    fact = str(fact)
    ans = 0
    for i in fact:
        ans += int(i)
    return ans

#Solution function
def Solution(num):
    start = time.time()
    
    ans = str(sumOfFactorialDigits(num))
    
    print 'The sum of the digits in the number ' + str(num) + '! is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 100
Solution(num)
