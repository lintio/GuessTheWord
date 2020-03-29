import random
from words import word_list

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

#select a random word from the list and changing it to upper case
word = random.choice(word_list).upper()

#setting up veriabled for later use
guessed_letters = []
guessed_words = []
attempts = 5
word_completion = '_' * len(word)
guessed = False
#loop until guessed is true or attempts = 0
while guessed == False:
    if attempts == 0:
        print(hangman[0])
        print('sorry you lost the word was', word)
        break
    else:
        #quick and dirty output to see if it is working
        print('letters guessed ', guessed_letters)
        print('words guessed ', guessed_words)
        print(hangman[attempts])
        print('\n')
        print(word_completion)
        #take the users input and makes it upper case
        guess = input('->').upper()
        if guess.isalpha():
            #checks to see if its a letter
            if len(guess) == 1:
                #check to see if it is in the guessed_letters array and the word
                if guess not in guessed_letters and guess not in word:
                    guessed_letters.append(guess)
                    attempts -= 1
                    print('sorry that letter is not in the word')
                elif guess in guessed_letters:
                    print('you have already guessed the letter', guess)
                else:
                    guessed_letters.append(guess)
                    for x, letter in enumerate(word):
                        if guess == letter:
                            word_completion = list(word_completion)
                            word_completion[x] = letter
                            word_completion = ''.join(word_completion)
                    if word_completion == word:
                        guessed = True
                        print('Well done You guessed the word!', word)
            if len(guess) == len(word):
                if guess not in guessed_words and guess != word:
                    guessed_words.append(guess)
                    attempts -= 1
                    print('Sorry, That is not the word')
                elif guess in guessed_words:
                    print('Sorry, You have already guessed', guess)
                else:
                    print('Well done You guessed the word!', word)
                    guessed = True
            else:
                print('Sorry, thats not a valid input')


