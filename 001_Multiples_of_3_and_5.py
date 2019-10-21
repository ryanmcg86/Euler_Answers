'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Link: https://projecteuler.net/problem=1'''

#Imports
import time

#Sum of multiples (of 3 and 5) function
def SumOfMults(n, mults):
    #Declare variables
    start = time.time()
    multiples = set()
    strnums = ''
    
    #Solve the problem
    for i in range(len(mults)):
        if i != len(mults) - 1:
            strnums += str(mults[i]) + ', '
        else:
            strnums = strnums[:-2]
            strnums += ' and ' + str(mults[i])
        for j in range(0, n, mults[i]):
            multiples.add(j)
    
    ans = str(sum(multiples))
    n = str(n)
            
    #Print the results
    print('The sum of all the multiples of ' + strnums)
    print('below ' + n + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
n = 1000
mults = [3, 5]
SumOfMults(n, mults)
