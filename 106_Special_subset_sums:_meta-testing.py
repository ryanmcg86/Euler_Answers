'''Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for 
any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, 
only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, 
only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?
Link: https://projecteuler.net/problem=106'''

#Imports
import time

#Build a function that calculates factorials
def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

#Build a function that calculates combinations
def comb(n, r):
    return fact(n) / (fact(r) * fact(n - r))

#Build a function that calculates how many subset pairs there are
def allsets(n):
    return str((3**n - 2**(n + 1) + 1) / 2)

#Build a function that calculates Catalan numbers
#Which count paths that don't cross the diagonal
def catalan(n):
    return int(comb(2 * n, n) / float(n + 1))

#Build a solve function
def solve(n):
    #Define variables
    start = time.time()
    ans = 0
    
    #Solve the problem
    for i in range(1, n / 2 + 1):
        ans += ((comb(2 * i, i) / 2.) - catalan(i)) * comb(n, 2 * i)
    
    ans = str(int(ans))
    sets = allsets(n)
    
    #Print the results
    print 'For n = ' + str(n) + ', ' + ans + ' of the ' + sets + ' subset pairs that '
    print 'can be obtained need to be tested for equality.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 12
solve(n)
