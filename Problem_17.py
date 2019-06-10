'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
Link: https://projecteuler.net/problem=17'''

#Imports
import time
import inflect

#Solution function
def Solution(num):
    start = time.time()
    p = inflect.engine()
    counter = 0
    
    for i in range(1, num + 1):
        counter += len(p.number_to_words(i).replace(' ', '').replace('-', '').replace(',', ''))
        
    print 'If all the numbers from 1 to ' + str(num) + ' inclusive were written out in words,'
    print str(counter) + ' letters would be used.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
num = 1000
Solution(num)
