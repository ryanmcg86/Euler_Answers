'''Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. 
Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
Link: https://projecteuler.net/problem=118'''

#Imports
import time
from itertools import permutations

#Build a binary function
def binary(n):
    bina = bin(n)[2:]
    while len(bina) < 8:
        bina = '0' + bina
    return bina + '0'

#Build a solve function
def solve():
    #Declare variables
    start = time.time()
    primesets = set()
    bins = []
    
    #Solve the problem
    for i in range(0, 256):
        bins.append(binary(i))
	
    for i in permutations(digits, 9):
        perm = ''.join(str(j) for j in i)
        for j in range(0, len(bins)):
            nums = ''
            for k in range(0, len(bins[j])):
                if bins[j][k] == '0':
                    nums += perm[k]
                else:
                    nums += ',' + perm[k]
            nums = nums.split(',')
            realnums = []
            for k in nums:
                if k != '':
                    realnums.append(int(k))
            realnums = sorted(realnums)
            allprimes = True
            for k in realnums:
                if isPrime(k) == False:
                    allprimes = False
                    break
            if allprimes:
                primesets.add(tuple(realnums))
                
    ans = str(len(primesets))
                
    #Print the results
    print 'There are ' + ans + ' distinct sets containing digits 1 - 9 '
    print 'where each element in the set is prime.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
