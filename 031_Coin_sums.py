'''In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1 × £1 + 1 × 50p + 2 × 20p + 1 × 5p + 1 × 2p + 3 × 1p
How many different ways can £2 be made using any number of coins?
Link: https://projecteuler.net/problem=31'''

#Imports
import time

#Build a answer function
def answer(coins):
    start = time.time()
    
    final = coins[-1]
    ways = [1] + [0] * final
    for coin in coins:
        for i in range(coin, final + 1):
            ways[i] += ways[i - coin]
    
    ans = str(ways[-1])
    coinstring = ''
    for i in range(0, len(coins)):
        if i != len(coins) - 1:
            coinstring += str(coins[i]) + 'p, '
        else:
            coinstring += 'and ' + str(coins[i]) + 'p'
    
    print 'There are ' + ans + ' different ways to make £' + str(final) + ' using any'
    print 'number of coins with values: ' + coinstring + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
coins = [1, 2, 5, 10, 20, 50, 100, 200]
answer(coins)
