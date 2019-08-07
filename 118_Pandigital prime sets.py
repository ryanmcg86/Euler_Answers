'''Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. 
Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
Link: https://projecteuler.net/problem=118'''

#Imports
import time
from itertools import permutations

#Build a partitions function
def partitions(n):
    po = [[()], [(1, )]]
    ans = []
    for num in range(2, n + 1):
        p = set()
        for i in range(num):
            for part in po[i]:
                p.add(tuple(sorted((num - i, ) + part)))
        po.append(list(p))
    for i in range(0, len(po[n])):
        ans.append(list(po[n][i])[::-1])
    return sorted(ans)

#Build a part function
def part(part, perm):
    temp = []
    index = 0
    for i in range(len(part)):
        num = ''
        for j in range(index, part[i] + index):
            if j < len(perm):
                num += str(perm[j])
        temp.append(int(num))
        index += part[i]
    return temp

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

#Build an allPrime function
def allPrime(part):
    for i in part:
        if isPrime(i) == False:
            return False
    return True

#Build a solve function
def solve(n):
    #Declare variables
    start = time.time()
    digits = [i + 1 for i in range(n)]
    answers = set()
    parts = partitions(n)
    
    #Solve the problem
    for i in permutations(digits):
        for j in range(0, len(parts)):
            nums = sorted(part(parts[j], i))
            if allPrime(nums):
                answers.add(tuple(nums))

    ans = str(len(answers))
                
    #Print the results
    print 'There are ' + ans + ' distinct sets containing digits 1 - ' + str(n)
    print 'where each element in the set is prime.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 9
solve(n)
