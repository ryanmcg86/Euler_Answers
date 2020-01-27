'''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
Link: https://projecteuler.net/problem=20'''

#Imports
import time

#Build a factorial function
def fact(n):
    return fact(n - 1) * n if n > 1 else 1

#Build a sum-of-factorial-digits function
def sumOfFactorialDigits(num):
    return sum(int(i) for i in str(fact(num)))

#Solution function
def solve(num):
    #Declare the variables
    start = time.time()
    
    #Solve the problem
    ans, n = str(sumOfFactorialDigits(num)), str(num)
    
    #Print the results
    print('The sum of the digits in the number ' + n + '! is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
num = 100
solve(num)
