'''The game Number Mind is a variant of the well known game Master Mind.

Instead of coloured pegs, you have to guess a secret sequence of digits. 
After each guess you're only told in how many places you've guessed the correct digit. 
So, if the sequence was 1234 and you guessed 2036, you'd be told that you have one correct digit; 
however, you would NOT be told that you also have another digit in the wrong place.

For instance, given the following guesses for a 5-digit secret sequence,

90342; 2 correct
70794; 0 correct
39458; 2 correct
34109; 1 correct
51545; 2 correct
12531; 1 correct

The correct sequence 39542 is unique.

Based on the following guesses,

5616185650518293; 2 correct
3847439647293047; 1 correct
5855462940810587; 3 correct
9742855507068353; 3 correct
4296849643607543; 3 correct
3174248439465858; 1 correct
4513559094146117; 2 correct
7890971548908067; 3 correct
8157356344118483; 1 correct
2615250744386899; 2 correct
8690095851526254; 3 correct
6375711915077050; 1 correct
6913859173121360; 1 correct
6442889055042768; 2 correct
2321386104303845; 0 correct
2326509471271448; 2 correct
5251583379644322; 2 correct
1748270476758276; 3 correct
4895722652190306; 1 correct
3041631117224635; 3 correct
1841236454324589; 3 correct
2659862637316867; 2 correct

Find the unique 16-digit secret sequence.
Link: https://projecteuler.net/problem=185'''

#Imports
import time
import copy
from itertools import combinations as combs

#Build a num_to_digits function
def num_to_digits(n):
    return [ord(c) - ord('0') for c in str(n)]

#Build a solve_a function
def solve_a(rules, a, L):
    new_rules = []
    for ri in range(len(rules)):
        if rules[ri][1] == 0:
            for p in range(L):
                a[p][rules[ri][0][p]] = 'N'
        else:
            new_rules.append(rules[ri])
    a = solve_r(new_rules, a, L)
    return a[0]

#Build a solve_r function
def solve_r(rules, a, L):
    positions = range(L)
    ri = 0
    for cp in combs(positions, rules[ri][1]):
        consistent = True
        for p in range(L):
            if p in cp:
                if a[p][rules[ri][0][p]] == 'N':
                    consistent = False
                    break
            else:
                if a[p][rules[ri][0][p]] == 'E':
                    consistent = False
                    break
            if not consistent:
                break
        if not consistent:
            continue
        saved_a = copy.deepcopy(a)
        for p in range(L):
            if p in cp:
                a[p][rules[ri][0][p]] = 'E'
                for d in range(10):
                    if d != rules[ri][0][p]:
                        a[p][d] = 'N'
            else:
                a[p][rules[ri][0][p]] = 'N'
        for ri2 in range(len(rules)):
            if ri != ri2:
                count_wrong = 0
                count_correct = 0
                for p in range(L):
                    if a[p][rules[ri2][0][p]] == 'E':
                        count_correct += 1
                    elif a[p][rules[ri2][0][p]] == 'N':
                        count_wrong += 1
                condition1 = count_correct > rules[ri2][1]
                condition2 = count_wrong > L - rules[ri2][1]
                if condition1 or condition2:
                    consistent = False
                    break
        if not consistent:
            a = saved_a
            continue
        saved_rule = rules.pop(ri)
        if len(rules):
            ans = solve_r(rules, a, L)
            if ans[1]:
                return ans
        else:
            answer = []
            for p in range(L):
                for d in range(10):
                    if a[p][d] == 'E' or a[p][d] == '?':
                        answer.append(str(d))
                        break
            return [''.join(answer), True]
        rules.insert(ri, saved_rule)
        a = saved_a
    return [str(0), False]

#Build a Solve function
def solve(rules):
    #Define variables
    start = time.time()
    L = len(str(rules[0][0]))
    rules = sorted(rules, key=lambda r: r[1])
    rules = [(num_to_digits(r[0]), r[1]) for r in rules]
    a = [['?'] * 10 for i in range(L)]
    ans = 0

    #Solve the problem
    ans = str(solve_a(rules, a, L))

    #Print the results
    print('The unique ' + str(L) + '-digit secret sequence is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
rules = [(5616185650518293, 2),
(3847439647293047, 1),
(5855462940810587, 3),
(9742855507068353, 3),
(4296849643607543, 3),
(3174248439465858, 1),
(4513559094146117, 2),
(7890971548908067, 3),
(8157356344118483, 1),
(2615250744386899, 2),
(8690095851526254, 3),
(6375711915077050, 1),
(6913859173121360, 1),
(6442889055042768, 2),
(2321386104303845, 0),
(2326509471271448, 2),
(5251583379644322, 2),
(1748270476758276, 3),
(4895722652190306, 1),
(3041631117224635, 3),
(1841236454324589, 3),
(2659862637316867, 2)]
solve(rules)
