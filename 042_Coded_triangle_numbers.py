'''The nth term of the sequence of triangle numbers is given by, 
t(n) = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English words, how many are triangle words?
Link: https://projecteuler.net/problem=42
LInk: https://projecteuler.net/project/resources/p042_words.txt'''

#Imports
import time

#Build a triangle number function
def t(n):
	return (n * (n + 1)) / 2

#Build a word Value function
def wordValue(word):
	return sum(ord(letter) - 64 for letter in word)
  
#Solution function
def solve(filename):
    start        = time.time()
    scores       = []
    triScores    = []
    n            = 1
    largestScore = 0
    counter      = 0

    words = list(open(filename, 'r').read().replace('"', '').split(','))

    for i in words:
        scores.append(wordValue(i))

    largestScore = max(scores)

    while t(n) < largestScore:
        triScores.append(t(n))
        n += 1

    for i in scores:
        if i in triScores:
            counter += 1
	
    print 'There are ' + str(counter) + ' triangle words in the file.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
filename = 'p042_words.txt'
solve(filename)
