import random
import string


options = int(input(''' Wellcome to the world of agents... No secret information (hahaha...)
         You will be given some options...
         Press 1 for coding your shit...   
         Press 2 to decode your hell...  
      '''))

if options == 1:    
# takes in the user text to code it
 given_text = input('Please do not enter your secret information here: ')
# this converts the text to words
 words = given_text.split()
#this portion converts the words to the letters
 def lett(randomletters, words):
# number of random letters
    modedwords = []
    for word in words:
    #putting the first to last letter
        ftol = word[1:]+word[0]
    #reversing the all letters
        reversedletters = ''.join(ftol[::-1])
    # add the random letter to the first and last of that word
        modified_word = [''.join(random.choices(string.ascii_lowercase, k=randomletters)) + reversedletters + ''.join(random.choices(string.ascii_lowercase, k=randomletters))]
        # puts all the modified words to the modedwords list[]
        modedwords.append(modified_word)
    #returns the moded words back 
    return modedwords
# assigned the number of random letters assigned before and after the word
 randomletters = 3   
# call the lett funtion and save the modified words to the mod 
 mod = lett(randomletters, words)
# takes the mod lists of list and put them to the list of strings
 wordlist = [item for sublist in mod for item in sublist]
# adds the string list to a para
 paragraph = ' '.join(wordlist[::-1])
 print(paragraph)


elif options == 2:
    text = input('Input your messed coded thing: ')
    for words in text:
        words = text.split()
    backreverse = words[::-1]
    reversed = backreverse
    # print(reversed)
    flipped = [(letters[::-1]) for letters in backreverse]
    # print(flipped)
    for word in flipped:
        halfwords = word[3:-3]
        corrected = halfwords[-1] + halfwords[:-1]
        print(corrected, end=' ')
else:
   raise ValueError ('you choose the different value')
  