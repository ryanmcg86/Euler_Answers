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
    largest, begin, end, xy = 0, 10**n - 1, 10**(n - 1) - 1, ''
    
    for i in range(begin, end, -1):
        for j in range(11 * (begin // 11), end, (-11 if i % 11 else -1)):
            p = i * j
            if p < largest: 
                break
            if isPal(p):
                if i * j > largest:
                    largest, xy = i * j, str(i) + ' and ' + str(j)
                break
                
    ans, n = str(largest), str(n)
            
    print('The largest palindrome made from the product ')
    print('of two ' + n + '-digit numbers, ' + xy + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')
    
#Run the program
n = 3
lpn(n)

'''Since the largest possible multiplication of 2 3-digit numbers (999 * 999) results in a 6-digit number,
we know that our palindrome will have 6 digits. Since a 6-digit palindrome must be of the following
form:

(100000 * a) + (10000 * b) + (1000 * c) + (100 * c) + (10 * b) + (1 * a)

which can be simplified as follows:

100000a + 10000b + 1000c + 100c + 10b + 1a

100001a + 10010b + 1100c

11(9091a + 910b + 100c)

We know that our palindrome must be divisible by 11, which means at least one of our two factors must
be divisible by 11.

I use this fact to speed up our search significantly.'''
