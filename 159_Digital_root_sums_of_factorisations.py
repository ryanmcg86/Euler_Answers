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

#Build a digital root sum function
def drs(x):
    ans = x
    while ans >= 10:
        tmp_sum = ans
        ans = 0
        while tmp_sum != 0:
            ans += tmp_sum % 10
            tmp_sum /= 10
    return ans
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    ans = 0
    mdrs = [0, 0]
    for i in range(2, limit + 1):
        mdrs.append(drs(i))
    
    #Solve the problem
    for a in range(2, limit + 1):
        b = 2
        while a * b <= limit and b <= a:
            c = mdrs[a] + mdrs[b]
            if mdrs[a * b] < c:
                mdrs[a * b] = c
            b += 1
            
    ans = str(sum(mdrs) - mdrs[limit])
    lim = str(limit)
    
    #Print the results
    print 'The sum of the maximum digital root sums '
    print 'for n in range 1 < n < ' + lim + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**6
solve(limit)
