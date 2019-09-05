'''Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed.
Examples are 'abc', 'hat' and 'zyx'.
When we study these three examples we see that for 'abc' two characters come lexicographically after its neighbour to the left.
For 'hat' there is exactly one character that comes lexicographically after its neighbour to the left. For 'zyx' there are zero 
characters that come lexicographically after its neighbour to the left.
In all there are 10400 strings of length 3 for which exactly one character comes lexicographically after its neighbour to the left.

We now consider strings of n ≤ 26 different characters from the alphabet.
For every n, p(n) is the number of strings of length n for which exactly one character comes lexicographically after its neighbour 
to the left.

What is the maximum value of p(n)?
Link: https://projecteuler.net/problem=158'''

#Imports
import time

#Build a factorial function
def fact(n):
    return fact(n - 1) * n if n > 1 else 1
    
#Build an nCr function
def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))
    
#Build a count function
def count(n, alphabet):
    if n > alphabet: return 0
    return sum(nCr(n, i) - 1 for i in range(1, n)) * nCr(alphabet, n)
   
#Build a Solve function
def solve(size):
    #Define variables
    start = time.time()
    alphabet = 26
    ans = 0
    nVal = 0
    
    #Solve the problem
    for i in range(2, size + 1):
        current = count(i, alphabet)
        if ans < current:
            ans = current
            nVal = i
            
    s = str(size)
    ans = str(ans)
    n = str(nVal)
    
    #Print the results
    print 'For strings of length n <= ' + s + ' different characters '
    print 'from the alphabet, where p(n) is the number of strings '
    print 'of length n for which exactly one character comes '
    print 'lexicographically after its neighbor to the left, '
    print 'the maximum value of p(n) is ' + ans + ', when n = ' + n + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
size = 26
solve(size)
