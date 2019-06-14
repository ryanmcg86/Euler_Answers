'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
Link: https://projecteuler.net/problem=22
LInk: https://projecteuler.net/project/resources/p022_names.txt'''

#Imports
import time

#Build a nameScore function
def nameScore(name, index):
    return sum(ord(letter) - 64 for letter in name) * (index + 1)

#Solution function
def Solution(filename):
    start = time.time()
    names = sorted(list(open(filename, 'r').read().replace('"', '').split(',')))
    total = sum(nameScore(names[i], i) for i in range(0, len(names)))
    
    print 'The total of all the name scores in the file is ' + str(total) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
filename = 'p022_names.txt'
Solution(filename)
