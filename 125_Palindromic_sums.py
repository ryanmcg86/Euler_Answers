'''The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 
6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, 
and the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned 
with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.
Link: https://projecteuler.net/problem=125'''

#Imports
import time

#Build an isPalindrome function
def isPal(n):
    return str(n) == str(n)[::-1]

#Build a Solve function
def Solve(limit):
    #Define variables
    start = time.time()
    nums = set()
    sqrtlimit = int(limit**0.5)
    
    #Solve the problem
    for i in range(1, sqrtlimit + 1):
        number = i**2
        for j in range(i + 1, sqrtlimit + 1):
            number += j**2
            if number > limit:
                break
            if isPal(number) and number not in nums:
                nums.add(number)
                
    ans = str(sum(nums))

    #Print the results
    print 'The sum of all palindromic sums under ' + str(limit) + ' that can '
    print 'be written as the sum of consecutive squares is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**8
Solve(limit)
