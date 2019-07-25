'''By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 
1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, 
RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and 
specify further that leading zeroes are not permitted, neither may a different letter have the same digital 
value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand 
common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an 
anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
Link: https://projecteuler.net/project/resources/p098_words.txt
Link: https://projecteuler.net/problem=98'''

#Imports
import time
from itertools import permutations as p

#Define an isAnagram function
#Returns whether two words are an anagram or not
def isAnagram(word1, word2):
    return sorted(word1) == sorted(word2)
    
    
#Define a Num function
#Returns a number created from a list of numbers
def Num(nums):
    return int(''.join(str(i) for i in nums))
    
#Define an isSquared function
#Returns whether a given number (in list form) can be squared
def isSquared(nums):
    num = Num(nums)
    return num**0.5 == int(num**0.5)
    
#Define the wordmap function
#Returns a wordmap for a given permutation and word
def wordMap(perm, word):
    wordmap = []
    wordlist = list(set(word))
    for i in range(0, len(wordlist)):
        wordmap.append([perm[i], wordlist[i]])
    return wordmap
    
#Define the buildNum function
#Returns the number (in list form) built with the word by using the wordmap
def buildNum(wordmap, word):
    number = []
    for i in range(0, len(word)):
        for j in range(0, len(wordmap)):
            if word[i] == wordmap[j][1]:
                number.append(wordmap[j][0])
    return number
    
#Define a maxSquare function that returns that max square for a word
#Returns the largest possible square formed by substituting numbers for letters
#among two words that form an anagram.
def maxSquare(word1, word2):
    maxsquare = 0
    uniqueCount = len(set(word1))
    perm = p([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], uniqueCount)
    wordlist = list(set(word1))
    for i in perm:
        wordmap = wordMap(i, word1)
        number1 = buildNum(wordmap, word1)
        number2 = buildNum(wordmap, word2)
        a = number1[0] != 0
        b = number2[0] != 0
        if isSquared(number1) and isSquared(number2) and a and b:
            squarenum = max(Num(number1), Num(number2))
            if squarenum > maxsquare:
                maxsquare = squarenum
    return maxsquare

#Build a solve function
def solve(filename):
    #Define variables
    start = time.time()
    anagrams = set()
    largestsquare = 0
    tempAnagrams = []
    f = open(filename, 'r')
    words = f.read().replace('"', '').split(',')
    
    #Solve the problem
    #Put the pairs of anagrams into the anagrams set
    for i in range(0, len(words)):
        anagram = []
        for j in range(i + 1, len(words)):
            if isAnagram(words[i], words[j]) and len(anagram) == 0:
                anagram.append(words[i])
                anagram.append(words[j])
            elif isAnagram(words[i], words[j]) and len(anagram) > 0:
                anagram.append(words[j])
        if len(anagram) > 0:
            anagrams.add(tuple(anagram))

    #Convert the anagrams set to a list
    anagrams = list(anagrams)

    #Narrow down anagrams to those words longer than 4 letters
    for i in range(0, len(anagrams)):
        if len(anagrams[i][0]) > 4:
            tempAnagrams.append(anagrams[i])

    #Reassign tempAnagrams to anagrams
    anagrams = tempAnagrams

    for i in range(0, len(anagrams)):
        number = maxSquare(anagrams[i][0], anagrams[i][1])
        if number > largestsquare:
            largestsquare = number
    
    #Print the results
    print 'The largest square number formed by any member '
    print 'of an anagramic pair from ' + filename + ' is ' + str(largestsquare) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
filename = 'p098_words.txt'
solve(filename)
