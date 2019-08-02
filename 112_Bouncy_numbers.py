'''Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
Link: https://projecteuler.net/problem=112'''

#Imports
import time

#Build an isInc function
def isInc(n):
    for i in range(len(str(n)) - 1):
        if str(n)[i] > str(n)[i + 1]:
            return False
    return True
    
#Build an isDec function
def isDec(n):
    for i in range(len(str(n)) - 1):
        if str(n)[i] < str(n)[i + 1]:
            return False
    return True
    
#Build an isBouncy function
def isBouncy(n):
    return isInc(n) == False and isDec(n) == False

#Build a solve function
def solve(frac):
    #Declare variables
    start = time.time()
    i = 1
    count = 0
    percent = count / float(i)
    
    #Solve the problem
    while percent != frac:
        if isBouncy(i):
            count += 1
        percent = count / float(i)
        i += 1
	
    ans = str(i - 1)
    frac = str(int(frac * 100)) + '%'
    
    #Print the results
    print 'The least number for which the proportion of '
    print 'bouncy numbers is exactly ' + frac + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
frac = 0.99
solve(frac)
