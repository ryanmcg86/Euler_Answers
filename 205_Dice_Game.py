'''Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. 
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? 
Give your answer rounded to seven decimal places in the form 0.abcdefg
Link: https://projecteuler.net/problem=205'''

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
