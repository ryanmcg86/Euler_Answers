'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Link: https://projecteuler.net/problem=1'''

#Imports
import time

#Sum of multiples (of 3 and 5) function
def SumOfMults(n, mults):
    start = time.time()
    multiples = set()
    strnums = ''
    for i in range(0, len(mults)):
        if i != len(mults) - 1:
            strnums += str(mults[i]) + ', '
        else:
            strnums = strnums[:-2]
            strnums += ' and ' + str(mults[i])
        for j in range(0, n, mults[i]):
            multiples.add(j)
    print 'The sum of all the multiples of ' + strnums + ' below ' + str(n) + ' is ' + str(sum(multiples)) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 1000
mults = [3, 5]
SumOfMults(n, mults)
