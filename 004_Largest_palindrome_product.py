'''A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
Link: https://projecteuler.net/problem=4'''

#Imports
import time

#isPal function
def isPal(n):
    return str(n) == str(n)[::-1]

#Largest palindromic number function
def lpn(n):
    start = time.time()
    largest = 0
    begin, end = 10**n - 1, 10**(n - 1) - 1
    
    for i in range(begin, end, -1):
        for j in range(begin, end, -1):
            if isPal(i * j):
                if i * j > largest:
                    largest = i * j
                break
                
    ans = str(largest)
    n = str(n)
            
    print('The largest palindrome made from the product ')
    print('of two ' + n + '-digit numbers is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Run the program
n = 3
lpn(n)
