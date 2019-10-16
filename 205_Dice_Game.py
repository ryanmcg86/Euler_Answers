'''A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.
We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.
How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?
Link: https://projecteuler.net/problem=204'''

#Imports
import time
import itertools
from math import prod as mul

#Build a Solve function
def solve(P, C):
    #Define variables
    start = time.time()
    a = [i for i in range(1, P[0] + 1)]
    b = [i for i in range(1, C[0] + 1)]
    peter = [[i, 0] for i in range(min(P[1], C[1]), mul(P) + 1)]
    colin = [[i, 0] for i in range(min(P[1], C[1]), mul(C) + 1)]
    denom = float(P[0]**P[1] * C[0]**C[1])
    ans = 0
	
    for p in itertools.product(a, repeat = P[1]):
        dice = sum(p)
        for i in peter:
            if i[0] == dice: i[1] += 1
    for c in itertools.product(b, repeat = C[1]):
        dice = sum(c)
        for i in colin:
            if i[0] == dice: i[1] += 1
    
    #Solve the problem
    for c in range(len(colin)):
        for p in range(c + 1, len(peter)):
            ans += peter[p][1] * colin[c][1]

    ans = str(round(ans / denom, 7))
    pete = str(P[1]) + ' ' + str(P[0]) + '-sided die'
    coli = str(C[1]) + ' ' + str(C[0]) + '-sided die'

    #Print the results
    print('The probability that Pyramidal Pete, with ' + pete + ', ')
    print('beats Cubic Colin, with ' + coli + ', is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
P = [4, 9]
C = [6, 6]
solve(P, C)
