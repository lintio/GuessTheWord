"""
import random
from words import word_list

#testing for selecting a random word from the list and changing it to upper case
selection = random.choice(word_list).upper()
word_completion = '_' * len(selection)
print(selection)
print(word_completion)
testInput = ''
#needed to add loop for better testing
while testInput != 'QUIT':
    testInput = input('->').upper()
    #first attempt at uisn enumerate seems cool and should be able to use it in my guess the word game
    for index, letter in enumerate(selection):
        if testInput == letter:
            print(index, letter)
            word_completion = list(word_completion)
            word_completion[index] = letter
            word_completion = ''.join(word_completion)
            print(word_completion)
"""

hangman = ["""
    /---\\
    |   |
    |   o
    |  /|\\
    |  / \\
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |  /|\\
    |  / 
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |  /|\\
    |  
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |  /|
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |  
    |  
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   
    |  
    |  
    |
   / \\____
   """]

print(hangman[5])

