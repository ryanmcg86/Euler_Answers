'''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of 
the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant 
numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of 
two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
Link: https://projecteuler.net/problem=23'''

#Imports
import time

#Build a proper divisor function
def pd(n):
    pd = [1]
    i = 2
    while i * i <= n:
        if n % i == 0:
            pd.append(i)
            if i != n / i:
                pd.append(n / i)
        i += 1
    return pd
    
#Build an isAbundant function
def isAbundant(n):
    return sum(pd(n)) > n

#Solution function
def Solution(num):
    start = time.time()
    total = 0
    abundants = []
    nums = [0] * (num + 1)
    
    for i in range(1, num + 1):
        if isAbundant(i):
            abundants.append(i)
            
    for i in abundants:
        for j in abundants:
            if i + j <= num:
                nums[i + j] = 1
                
    for i in range(1, num + 1):
        if nums[i] == 0:
            total += i
    
    print 'The sum of all the positive integers which cannot be written as the '
    print 'sum of two abundant numbers is ' + str(total)
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 28123
Solution(num)
