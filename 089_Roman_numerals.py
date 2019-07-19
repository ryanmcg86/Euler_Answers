'''For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of 
writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, 
as it uses the least number of numerals.

The 11K text file, roman.txt, contains one thousand numbers written in valid, 
but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
Link: https://projecteuler.net/project/resources/p089_roman.txt
Link: https://projecteuler.net/about=roman_numerals
Link: https://projecteuler.net/problem=89'''

#Imports
import time

#Build a solve function
def solve(filename):
    #Define variables
    start = time.time()
    f = open(filename, 'r')
    numerals = f.read().split('\n')
    ans = 0

    #Solve the problem	
    for i in range(0, len(numerals)):
        if 'CCCC' in numerals[i]:
            if 'DCCCC' in numerals[i]: ans += 3
            else: ans += 2
        if 'XXXX' in numerals[i]:
            if 'LXXXX' in numerals[i]: ans += 3
            else: ans += 2
        if 'IIII' in numerals[i]:
            if 'VIIII' in numerals[i]: ans += 3
            else: ans += 2
            
    ans = str(ans)

    #Print the results
    print 'The number of characters saved by writing each of '
    print 'these roman numerals in their minimal form is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
filename = 'roman.txt'
solve(limit)
