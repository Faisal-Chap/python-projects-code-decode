# Write a python program to translate a message into secret code language. 
#Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter 
#and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter 
#and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string
text = input("Please enter a bit of text: ")
words = text.split()
# randomletters = ''.join(random.choices(ascii, k=3))
num_letters = 3
new_words = [words + ''.join(random.choices(string.ascii_lowercase, k=num_letters))]

# modword = "".join(random.)
print(new_words)
# para = ' '.join(words)
# print(para)
