'''Let p(n) represent the number of different ways in which n coins can be separated into piles. 
For example, five coins can be separated into piles in exactly seven different ways, so p(5) = 7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
Link: https://projecteuler.net/problem=78'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    part = [1, 1, 2]
    ans = 0
    
    #Solve the problem
    while True:
        val = 0
        n = len(part)
        for dk in [-1, 1]:
            k = dk
            while True:
                i = n - (k * (3 * k - 1)) // 2
                if i < 0:
                    break
                if k % 2 != 0:
                    val += part[i]
                else:
                    val += -1 * part[i]
                k += dk
        val %= limit
        if val == 0:
            ans = str(len(part))
            break
        part.append(val)
    
    #Print the results
    print 'The least value of n for which p(n) '
    print 'is divisible by ' + str(limit) + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
limit = 10**6
solve(limit)
