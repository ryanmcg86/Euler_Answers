'''The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
Link: https://projecteuler.net/problem=36'''

#Imports
import time

#Build an isPalindrome function
def isPalindrome(num):
    return str(num) == str(num)[::-1]
    
#Build a binary function
def binary(num):
    return bin(num)[2:]

#Build a Solve function
def Solve(num):
    start = time.time()
    
    total = 0
    for i in range(1, num):
        if isPalindrome(i) and isPalindrome(binary(i)):
            total += i
            
    total = str(total)
    
    print 'The sum of all numbers, less than ' + str(num) + ','
    print 'which are palindromic in base 10 and base 2 is ' + total + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 1000000
Solve(num)
