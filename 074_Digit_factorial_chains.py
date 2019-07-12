'''The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain 
with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
Link: https://projecteuler.net/problem=74'''

#Imports
import time
from itertools import combinations_with_replacement as cwr
from itertools import permutations as p

#Build a factorial function
def fact(n):
    return [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880][n]
    
#Build a sum-factorials function
def sumFacts(n):
    return sum(fact(int(i)) for i in str(n))
    
#Build a countChains function
def countChains(n):
    num = sumFacts(n)
    distincts = [n]
    while num not in distincts:
        if num not in distincts:
            distincts.append(num)
        num = sumFacts(num)
    return len(distincts)
    
#Build a countAnswers function
def countAnswers(answers):
    unique = []
    for ans in answers:
        #Deal with 1's in an answer since fact(0) and fact(1) both equal 1.
        num = ''
        for i in range(0, len(str(ans))):
            if str(ans)[i] == '1':
                num = str(ans)[0:i] + '0' + str(ans)[i + 1:]
            else:
                num = str(ans)
            perms = p(num)
            for i in list(perms):
                num = int(''.join(str(i[j]) for j in range(len(list(i)))))
                #Only insert new permutations that don't have leading 0's.
                if i not in unique and len(str(num)) == len(str(ans)):
                    unique.append(i)
        #Deal with 0's in an answer since fact(0) and fact(1) both equal 1.
        num = ''
        for i in range(0, len(str(ans))):
            if str(ans)[i] == '0':
                num = str(ans)[0:i] + '1' + str(ans)[i + 1:]
            else:
                num = str(ans)
            perms = p(num)
            for i in list(perms):
                num = int(''.join(str(i[j]) for j in range(len(list(i)))))
                #Only insert new permutations that don't have leading 0's.
                if i not in unique and len(str(num)) == len(str(ans)):
                    unique.append(i)
    return str(len(unique))

#Build a solve function
def solve(limit, left, right):
    #Define variables
    start   = time.time()
    digits  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answers = []
    ans     = 0
    
    #Solve the problem
    for i in range(1, len(str(limit))):
        comb = cwr(digits, i)
        for j in comb:
            num = int(''.join(str(j[k]) for k in range(i)))
            if countChains(num) == chainCount and num not in answers:
                answers.append(num)

    ans = countAnswers(answers)

    #Print the results
    print 'There are ' + ans + ' chains containing exactly ' + str(chainCount) + ' non-'
    print 'repeating terms, with a starting number below ' + str(limit) + '.'
    print 'It took ' + str(time.time() - start) + ' seconds to find the result.'

#Run the program
limit = 10**6
chainCount = 60
solve(limit, chainCount)
