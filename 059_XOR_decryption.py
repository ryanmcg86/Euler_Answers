'''Each character on a computer is assigned a unique code and the preferred standard is ASCII 
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, 
and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte 
with a given value, taken from a secret key. The advantage with the XOR function is that using the 
same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key 
is made up of random bytes. The user would keep the encrypted message and the encryption key in 
different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a 
password as a key. If the password is shorter than the message, which is likely, the key is 
repeated cyclically throughout the message. The balance for this method is using a sufficiently 
long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted 
ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the 
message and find the sum of the ASCII values in the original text.
Link: https://projecteuler.net/problem=59'''

#Imports
import time

#Build a decrypt function
def xorDecrypt(words):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = list(letters)
    for i in letters:
        for j in letters:
            for k in letters:
                key = i + j + k
                decrypt = []
                for position in range(0, len(words)):
                    decrypt.append(words[position] ^ ord(key[position % len(key)]))
                decrypt = ''.join(chr(word) for word in decrypt)
                if " the " in decrypt and " and " in decrypt:
                    return decrypt
    return ''

#Build a solve function
def solve(file):
    #Define variables
    start = time.time()
    ans = 0
    f = open(file, 'r')
    words = [int(k) for k in f.read().split(',')]
    f.close()

    #Solve the problem
    decrypt = xorDecrypt(words)
    for word in decrypt:
        ans += ord(word)

    #Print the results
    print 'The sum of the ASCII values in the decrypted version of the original text is ' + str(ans) + '.'
    print 'Here is that original text: \n'
    print decrypt
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
file = 'cipher.py'
solve(file)
