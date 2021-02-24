'''We define an S-number to be a natural number, n, that is a perfect square and its square 
root can be obtained by splitting the decimal representation of n into 2 or more numbers 
then adding the numbers.

For example, 81 is an S-number because rad(81) = 8 + 1.
6724 is an S-number: rad(6724) = 6 + 72 + 4.
8281 is an S-number: rad(8281) = 8 + 2 + 81 = 82 + 8 + 1.
9801 is an S-number: rad(9801) = 98 + 0 + 1.

Further we define T(N) to be the sum of all S numbers n <= N. You are given T(10**4) = 41333.

Find T(10**12)
Link: https://projecteuler.net/problem=719'''

#Imports
import time
from itertools import combinations as co

#Build a memo dictionary for memoization
memo = {}

#Build a combos function
def combos(num):
	if len(str(num)) not in memo:
		combos = []
		for i in range(1, len(str(num))):
			for j in co([k for k in range(1, len(str(num)))], i):
				combos.append(list(j))
		memo[len(str(num))] = combos
	return memo[len(str(num))]

#Build a sums function
def sums(num):
	combs = combos(num)

	numList = [i for i in str(num)]
	sums = []

	for c in combs:
		new = []
		for i in range(len(numList)):
			if i in c:
				new.append(',')
			new.append(numList[i])
		sums.append(sum([int(i) for i in ''.join(new).split(',')]))

	return sorted(sums)

#Build an isS function
def isS(num):
	s = sums(num)
	return int(num)**0.5 in s

#Build a T(N) function
def T(N):
	total = 0
	for i in range(1, int(N**0.5) + 1):
		if i % 9 == 0 or i % 9 == 1:
			if isS(i**2):
				total += i**2
	return total

#Sum of multiples (of 3 and 5) function
def solution(N):
    #Declare variables
    start = time.time()
    
    #Solve the problem
    ans = str(T(N))
            
    #Print the results
    print('T(' + str(N) + ') = ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
N = 10**12
solution(N)
