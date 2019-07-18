'''In the game, Monopoly, the standard board is set up in the following way:

GO  A1  CC1 A2  T1  R1  B1  CH1 B2  B3 JAIL
H2                                       C1
T2                                       U1
H1                                       C2
CH3                                      C3
R4                                       R2
G3                                       D1
CC3                                     CC2
G2                                       D2
G1                                       D3
G2J F3  U2  F2  F1  R3  E3  E2  CH2  E1  FP

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of 
squares they advance in a clockwise direction. Without any further rules we would expect to visit each square 
with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, 
if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. 
Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a 
card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. 
There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; 
any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of 
finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for 
which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a 
movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. 
We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about 
requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to 
produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, 
E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the 
six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
Link: https://projecteuler.net/problem=84'''

#Imports
import time
from random import *

def solve(dice):
    #Declare variables
    start  = time.time()
    i      = 0         #Community Chest deck index
    j      = 0         #Chance deck index
    p      = 0         #Game board index
    d      = 0         #Doubles counter
    counts = [0] * 40  #Landing spots tracker
    ans    = ''        #six-digital modal string
    maxes  = [0, 0, 0] #List that stores the 3 largest amounts a spot was landed on  
	
    #Solve the problem
    for x in range(0, 5 * 10**5):
        #Dice rolls
        a = randint(1, dice)
        b = randint(1, dice)

        #Count doubles
        if a == b:
            d += 1
        else:
            d = 0

        #Send to jail on 3rd double
        if d == 3:
            p = 10
            d = 0
            counts[p] += 1
            continue

        #Define the destination
        dest = p + a + b

        #Account for the board looping
        if dest > 39:
            dest -= 40

        #Go to jail check
        if dest == 30:
            p = 10
            counts[p] += 1
            continue

        #Community Chest
        if dest == 2 or dest == 17 or dest == 33:
            #Set next card in the Community Chest deck
            i += 1
            #Reset the Community Chest deck
            if i == 17:
                i = 1
            #Community Chest outcomes
            cc = [0, 10]
            if i - 1 < len(cc):
                p = cc[i - 1]
                counts[p] += 1
                continue

        #Chance
        if dest == 7 or dest == 22 or dest == 36:
            #Set next card in the Chance deck
            j += 1
            #Reset the Chance deck
            if j == 17:
                j = 1
            #Chance outcomes
            chance = [0, 10, 11, 24, 39, 5, dest - 3]
            if j - 1 < len(chance):
                p = chance[j - 1]
                counts[p] += 1
                continue
            if j == 8 or j == 9:
                if dest == 7:
                    p = 15
                if dest == 22:
                    p = 25
                if dest == 36:
                    p = 5
                counts[p] += 1
                continue
            if j == 10:
                if dest == 7 or dest == 36:
                    p = 12
                if dest == 22:
                    p = 28
                counts[p] += 1
                continue

        p = dest
        counts[p] += 1
        continue
	
    #Find the 3 highest values
    t = counts
    maxes[0] = max(t)
    for x in range(0, 2):
        t = [t[i] for i in range(0, len(t)) if t[i] != maxes[x]]
        maxes[x + 1] = max(t)
    for x in range(0, len(maxes)):
	num = counts.index(maxes[x])
        if num < 10:
            ans += '0' + str(num)
	else:
            ans += str(num)

    #Print the results
    print 'When using a ' + str(dice) + '-sided dice, the six-digital modal string is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
dice = 4
solve(dice)
