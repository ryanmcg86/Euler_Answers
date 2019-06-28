'''The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
Link: https://projecteuler.net/problem=48'''

#Imports
import time

#Build a solve function
def solve(digits, number):
    #Declare variables
    start = time.time()
    ans = str(sum(i**i for i in range(1, number + 1)))[-digits:]

    #Print the results
    print 'The last ' + str(digits) + ' digits of the series,'
    print '1^1 + 2^2 + 3^3 + ... + ' + str(number) + '^' + str(number) + ' are ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'


#Run the program
digits = 10
number = 1000
solve(digits, number)
