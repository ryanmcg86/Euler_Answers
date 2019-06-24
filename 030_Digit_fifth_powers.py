'''Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
Link: https://projecteuler.net/problem=30'''

#Imports
import time

#Build a suffix function
def buildSuffix(num):
    suff  = 'th'
    begin = len(str(num)) - 2
    end   = begin + 1
    suffixes = [[1, 'st'], [2, 'nd'], [3, 'rd']]
    if str(num)[begin:end] != '1':
        for i in range(0, len(suffixes)):
            if int(str(num)[-1]) == suffixes[i][0]:
                   suff = suffixes[i][1]
    return suff

#Build an isPower function
def isPower(num, power):
    return num == sum(int(digit)**power for digit in str(num))

#Build a answer function
def answer(power):
    start = time.time()
    
    powers = []
    
    for i in range(10, 9**(power + 1) + 1):
        if isPower(i, power):
            powers.append(i)
            
    suff = buildSuffix(power)
    power = str(power) + suff
    
    print 'The sum of all the numbers that can be written as the sum of ' 
    print power + ' powers of their digits is ' + str(sum(powers)) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
power = 5
answer(power)
