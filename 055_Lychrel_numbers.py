'''If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213,
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
Due to the theoretical nature of these numbers, and for the purpose of this problem, 
we shall assume that a number is Lychrel until proven otherwise. In addition you are given that f
or every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, 
or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. 
In fact, 10677 is the first number to be shown to require over fifty iterations before producing 
a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
Link: https://projecteuler.net/problem=55'''

#Imports
import time

#Build an isPalindrome function
def isPal(n):
    return n == int(str(n)[::-1])
  
#Build a Reverse function
def rev(n):
    return int(str(n)[::-1])
    
#Build an isLychrel function
def isLychrel(n):
    num = n
    for i in range(0, 50):
        num += rev(num)
        if isPal(num):
            return False
    return True

#Build a solve function
def solve(n):
    #Define variables
    start = time.time()
    counter = 0

    #Solve the problem
    for i in range(1, n):
        if isLychrel(i):
            counter += 1

    #Print the results
    print 'There are ' + str(counter) + ' Lychrel numbers below ' + str(n) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 10000
solve(n)
