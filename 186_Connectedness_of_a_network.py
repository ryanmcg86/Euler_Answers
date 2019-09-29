'''Here are the records from a busy telephone system with one million users:

RecNr Caller  Called
1     200007  100053
2     600183  500439
3     600863  701497
...   ...     ...
The telephone number of the caller and the called number in record n are 
Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)
For 56 ≤ k, Sk = [Sk-24 + Sk-55] (modulo 1000000)

If Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are friends if X calls Y or vice-versa. 
Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.

The Prime Minister's phone number is 524287. After how many successful calls, not counting misdials, 
will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?
Link: https://projecteuler.net/problem=186'''

#Imports
import time

#Build a "Lagged Fibonacci Generator"
def lfg():
    s = [0 for i in range(56)]
    for k in range(1, 56):
        s[k] = (100003 - 200003 * k + 300007 * k**3) % 10**6
        yield s[k]
    k = 56
    while True:
        s[k % 56] = (s[(k - 24) % 56] + s[(k - 55) % 56]) % 10**6
        yield s[k % 56]
        k += 1

#Build a Solve function
def solve(pm):
    #Define variables
    start = time.time()
    generator = lfg()
    callers = [-1 for i in range(10**6)]
    callers[pm] = 0
    groups = [[pm]]
    empty = []
    calls = 0

    #Solve the problem
    while len(groups[0]) < 990000:
        x = next(generator)
        y = next(generator)
        if x == y: continue
        calls += 1
        if callers[x] < 0 and callers[y] < 0:
            if len(empty) > 0:
                g = empty.pop()
                groups[g] = [x, y]
            else:
                g = len(groups)
                groups.append([x, y])
            callers[x] = g
            callers[y] = g
        elif callers[y] < 0:
            callers[y] = callers[x]
            groups[callers[x]].append(y)
        elif callers[x] < 0:
            callers[x] = callers[y]
            groups[callers[y]].append(x)
        elif callers[x] != callers[y]:
            if callers[y] < callers[x]: x, y = y, x
            gx, gy = callers[x], callers[y]
            for c in groups[gy]: callers[c] = gx
            groups[gx] += groups[gy]
            groups[gy] = []
            empty.append(gy)
	
    generator.close()
    ans = str(calls)

    #Print the results
    print('After ' + ans + ' calls, 99% of the users (including the PM) ')
    print('will be a friend, or a friend of a friend etc., of the PM.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
pm = 524287
solve(pm)
