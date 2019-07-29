'''Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if 
for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, 
whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair 
combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven 
to twelve elements (the two examples given above are the first two sets in the file), identify all the special 
sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.
Link: https://projecteuler.net/problem=105'''

#Imports
import time
from itertools import combinations as c

#Build an isSpecial function
def isSpecial(A):
    for i in range(1, len(A) + 1):
        for j in c(A, i):
            setB = set(j)
            temp = A - setB
            for k in range(1, len(temp) + 1):
                for l in c(temp, k):
                    setC = set(l)
                    if len(setB) > len(setC):
                        if sum(setB) <= sum(setC):
                            return False
                    if sum(setB) == sum(setC):
                        return False
    return True

#Build a solve function
def solve(filename):
    #Define variables
    start = time.time()
    ans = 0
    f = open(filename, 'r')
    sets = f.read().split('\n')
  
    for i in range(0, len(sets)):
        sets[i] = sets[i].split(',')

    for i in range(0, len(sets)):
        for j in range(0, len(sets[i])):
            sets[i][j] = int(sets[i][j])

    for i in range(0, len(sets)):
        sets[i] = set(sets[i])
        
    #Solve the problem
    for i in range(0, len(sets)):
        if isSpecial(sets[i]):
            ans += sum(sets[i])
    
    #Print the results
    print 'Using ' + filename + ', the sum of the special sets is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
filename = 'sets.txt'
solve(filename)
