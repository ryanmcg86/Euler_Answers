'''Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for 
any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. 
The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form 
B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, 
with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. 
The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.
Link: https://projecteuler.net/problem=103'''

#Imports
import time
from itertools import combinations as comb

def isSpecial(A):
    for i in range(1, len(A) + 1):
        for j in comb(A, i):
            setB = set(j)
            temp = A - setB
            for k in range(1, len(temp) + 1):
                for l in comb(temp, k):
                    setC = set(l)
                    if len(setB) > len(setC):
                        if sum(setB) <= sum(setC):
                            return False
                    if sum(setB) == sum(setC):
                        return False
    return True

#Build a solve function
def solve():
    #Define variables
    start = time.time()
    n6 = [11, 18, 19, 20, 22, 25]
    n7 = [20] + [20 + n6[i] for i in range(len(n6))]
    ans = ''.join(str(i) for i in n7)
    minsum = sum(n7)
    
    #Solve the problem
    for a in range(n7[0] - 3, n7[0] + 4):
        for b in range(n7[1] - 3, n7[1] + 4):
            for c in range(n7[2] - 3, n7[2] + 4):
                for d in range(n7[3] - 3, n7[3] + 4):
                    for e in range(n7[4] - 3, n7[4] + 4):
                        for f in range(n7[5] - 3, n7[5] + 4):
                            for g in range(n7[6] - 3, n7[6] + 4):
                                test = [a, b, c, d, e, f, g]
                                if test != sorted(test):
                                    continue
                                if len(test) != len(set(test)):
                                    continue
                                if isSpecial(set(test)):
                                    if sum(test) < minsum:
                                        minsum = sum(test)
                                        ans = ''.join(str(i) for i in test)
                                        
    #Print the results
	print 'The set string for A, the optimum special '
	print 'sum set for n = 7 is ' + ans + '.'
	print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
