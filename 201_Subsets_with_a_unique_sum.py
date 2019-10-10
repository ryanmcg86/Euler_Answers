'''For any set A of numbers, let sum(A) be the sum of the elements of A.
Consider the set B = {1,3,6,8,10,11}.
There are 20 subsets of B containing three elements, and their sums are:

sum({1,3,6}) = 10,
sum({1,3,8}) = 12,
sum({1,3,10}) = 14,
sum({1,3,11}) = 15,
sum({1,6,8}) = 15,
sum({1,6,10}) = 17,
sum({1,6,11}) = 18,
sum({1,8,10}) = 19,
sum({1,8,11}) = 20,
sum({1,10,11}) = 22,
sum({3,6,8}) = 17,
sum({3,6,10}) = 19,
sum({3,6,11}) = 20,
sum({3,8,10}) = 21,
sum({3,8,11}) = 22,
sum({3,10,11}) = 24,
sum({6,8,10}) = 24,
sum({6,8,11}) = 25,
sum({6,10,11}) = 27,
sum({8,10,11}) = 29.

Some of these sums occur more than once, others are unique.
For a set A, let U(A,k) be the set of unique sums of k-element subsets of A, in our example we find 
U(B,3) = {10,12,14,18,21,25,27,29} and sum(U(B,3)) = 156.

Now consider the 100-element set S = {1^2, 2^2, ... , 100^2}.
S has 100891344545564193334812497256 50-element subsets.

Determine the sum of all integers which are the sum of exactly one of the 50-element subsets of S, i.e. 
find sum(U(S,50)).
Link: https://projecteuler.net/problem=201'''


#General solution (only works in reasonable time for smaller sets)
#------------------------------------------------------
#Imports
import time
from itertools import combinations as c

#Build a U function
def U(A, k):
    ans = set()
    for i in c(A, k):
        total = sum(i)
        if total in ans: ans.remove(total)
        else:            ans.add(total)
    return ans

#Build a Solve function
def solve(A, k):
    #Define variables
    start = time.time()
  
    #Solve the problem
    ans = str(sum(U(A, k)))

    #Print the results
    print('Sum(U(A, ' + str(k) + ')) = ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
A = (i**2 for i in range(1, 101))
k = 50
solve(A, k)
#------------------------------------------------------
#Specific solution (only works for a set of squared numbers from 1 to n)
#------------------------------------------------------
#Imports
import time

#Build a Solve function
def solve(setSize, sumSize):
    #Define variables
    start = time.time()
    n, m = setSize, sumSize
    one  = [[0 for j in range(m + 1)] for i in range(n + 1)]
    many = [[0 for j in range(m + 1)] for i in range(n + 1)]
    
    #Solve the problem
    for i in range(n + 1):
        one[i][0] = 1
        for j in range(1, min(i, m) + 1):
            z = many[i - 1][j]
            y = (many[i - 1][j - 1] << (i**2))
            x = one[i - 1][j] & (one[i - 1][j - 1] << (i**2))
            many[i][j] = z | y | x
            z = one[i - 1][j]
            y = (one[i - 1][j - 1] << (i**2))
            w = sum(k**2 for k in range(i + 1))
            x = ((1 << (1 + w)) - 1 - many[i][j])
            one[i][j] = (z | y) & x

    r = reversed(format(one[n][m], 'b'))
    ans = str(sum(x for x,b in enumerate(r) if b == '1'))
	
    n, m = str(n), str(m)
    
    #Print the results
    print('When A is a set with values i^2 for ')
    print('1 <= i <= 100, Sum(U(A, ' + m + ')) = ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
setSize = 100
sumSize = 50
solve(setSize, sumSize)
