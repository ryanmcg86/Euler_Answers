'''A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" 
and numbering the tiles 2 to 7 in an anti-clockwise direction.

New rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on. 
The diagram below shows the first three rings.

By finding the difference between tile n and each of its six neighbours we shall define PD(n) to be the 
number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.

It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.

Find the 2000th tile in this sequence.
Link: https://projecteuler.net/problem=128'''

#Imports
import time

#Build a suffix function
def buildSuffix(num):
    suffs = ['th', 'st', 'nd', 'rd']
    suff = suffs[0]
    begin = len(str(num)) - 2
    end = begin + 1
    if str(num)[begin:end] != '1':
        lastdigit = int(str(num)[-1])
        if lastdigit < len(suffs):
            suff = suffs[lastdigit]
    return suff
    
#Build an isPrime function
def isPrime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#Build a Solve function
def Solve(limit):
    #Define variables
    start = time.time()
    count = 1
    n = 0
    ans = 0
    
    #Solve the problem
    while count < limit:
        n += 1
        a = isPrime(6 * n - 1)
        b = isPrime(6 * n + 1)
        c = isPrime(12 * n + 5)
        if a and b and c:
            count += 1
            ans = (3 * n**2 - 3 * n + 2)
            if count >= limit:
                break
        b = isPrime(6 * n + 5)
        c = isPrime(12 * n - 7)
        if a and b and c and n != 1:
            count += 1
            ans = (3 * n**2 + 3 * n + 1)
            
    limit = str(limit) + buildSuffix(limit)
    ans = str(ans)
        
    #Print the results
    print 'If all of the tiles for which PD(n) = 3 are listed in ascending '
    print 'order to form a sequence, the ' + limit + ' number is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 2000
Solve(limit)
