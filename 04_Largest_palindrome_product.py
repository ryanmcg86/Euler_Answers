'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
Link: https://projecteuler.net/problem=4'''

#Imports
import time

#isPal function
def isPal(n):
    return str(num) == str(num)[::-1]

#Largest palindromic number function
def lpn(n):
    start = time.time()
    largest = 0
    begin = ''
    for i in range(0, n):
        begin.append('9')
    end   = int(begin[:-1])
    begin = int(begin)
    
    for i in range(begin, end, -1):
        for j in range(begin, end, -1):
            if isPal(i * j):
                if i * j > largest:
                    largest = i * j
                break
            
    print 'The largest palindrome made from the product of two ' + str(n) + '-digit numbers is ' + str(largest) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 3
lpn(n)
