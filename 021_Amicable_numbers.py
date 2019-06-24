'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
Link: https://projecteuler.net/problem=21'''

#Imports
import time

#Build a d(n) function which returns the sum
#of proper divisors of n
def d(n):
    ans = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            ans += i
    return ans
    
#Build an isAmicable function
def isAmicable(n):
    return d(num1) == n and d(n) != n

#Solution function
def Solution(num):
    start = time.time()
    
    amicable = []
    for i in range(1, num):
        if isAmicable(i):
            amicable.append(i)
    
    print 'The sum of all amicable numbers under ' + str(num) + ' is ' + str(sum(amicable)) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 10000
Solution(num)
