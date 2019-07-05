'''In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). 
But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); 
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	      Player 2	 	         Winner
1	 	    5H 5C 6S 7S KD    2C 3S 8S 8D TD      Player 2
        Pair of Fives     Pair of Eights

2	 	    5D 8C 9S JS AC    2C 5C 7D 8S QH      Player 1
        Highest card Ace  Highest card Queen

3	 	    2D 9C AS AH AC    3D 6D 7D TD QD      Player 2
        Three Aces        Flush with Diamonds
 	
4	 	    4D 6S 9H QH QC    3D 6D 7H QD QS      Player 1
        Pair of Queens    Pair of Queens
        Highest card Nine Highest card Seven

5	 	    2H 2D 4C 4D 4S    3C 3D 3S 9S 9D      Player 1
        Full House        Full House
        With Three Fours  with Three Threes
 	
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
Link: https://projecteuler.net/problem=54'''

#Imports
import time

#Build a Straight function
def straight(nums):
	if nums == [14, 2, 3, 4, 5]:
		return 5
	if not sum([abs(nums[i] - nums[0] - i) for i in range(5)]):
		return nums[-1]
	return False

#Build a Flush function
def flush(suits):
	return len(set(suits)) == 1

#Build a Groups function
def groups(nums):
	groups = []
	for n in set(nums):
		groups.append((nums.count(n), n))
	groups.sort()
	groups.reverse()
	return groups

#Build a hand function
def hand(cards):
	cards.sort()
	nums      = [c[0] for c in cards]
	suits     = [c[1] for c in cards]
	s, f      = straight(nums), flush(suits)
	of_a_kind = [count for count, value in groups(nums)]
	signature = [value for count, value in groups(nums)]
	if s and f:
		return 8, s
	if of_a_kind == [4, 1]:
		return 7, signature
	if of_a_kind == [3, 2]:
		return 6, signature
	if f:
		return 5, signature
	if s:
		return 4, signature
	if of_a_kind == [3, 1, 1]:
		return 3, signature
	if of_a_kind == [2, 2, 1]:
		return 2, signature
	if of_a_kind == [2, 1, 1, 1]:
		return 1, signature
	return 0, signature

#Build a solve function
def solve(file):
    #Define variables
    start = time.time()
    count = 0
    vals = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
	
    #Fill the values
    for i in range(2, 10):
	vals[str(i)] = i
    
	
    #Solve the problem
    for h in [line.split() for line in open(file, 'r').xreadlines()]:
	p1 = [(vals[a], b) for a, b in h[:5]]
	p2 = [(vals[a], b) for a, b in h[5:]]
	if hand(p1) > hand(p2):
		count += 1

    #Print the results
    print 'Player 1 wins ' + str(count) + ' hands.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
file = 'poker.txt'
solve(file)
