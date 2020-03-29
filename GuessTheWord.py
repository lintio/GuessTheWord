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
    |   |
    |  
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
    |   
    |   
    |  
    |  
    |
   / \\____
   """,
   """
    /
    |   
    |   
    |  
    |  
    |
   / \\____
   """,
   """
    
       
       
      
      
    
   / \\____
   """,
   """
    
       
       
      
      
    
   _______
   """,
   """
    
       
       
      
      
    
   _
   """]

def selectWord(word_lenght):
    #select a random word from the list and changing it to upper case
    word = random.choice(word_list).upper()
    while len(word) > word_lenght:
        word = random.choice(word_list).upper()
    return(word)

def play(word, level):
    #setting up veriabled for later use
    guessed_letters = []
    guessed_words = []
    attempts = level
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
                        #checks if the letter is in the word by converting the word to a list and then back again
                        for x, letter in enumerate(word):
                            if guess == letter:
                                word_completion = list(word_completion)
                                word_completion[x] = letter
                                word_completion = ''.join(word_completion)
                        #checks to see if all letters have been guessed
                        if word_completion == word:
                            guessed = True
                            print('Well done You guessed the word!', word)
                #allows the player to guess the word as a whole
                elif len(guess) == len(word):
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

def menu():
    menu_select = 5
    word_lenght = 10
    trys = 5
    while menu_select != 3:
        print('Current settings - Max Word Lenght =', word_lenght, ' & trys =', trys, '-')
        print('1) Play')
        print('2) Change Settings')
        print('3) Quit')
        menu_select = input('->')
        if menu_select.isdigit():
            menu_select = int(menu_select)
            if menu_select == 3:
                break
            elif menu_select == 1:
                word = selectWord(word_lenght)
                play(word, trys)
            elif menu_select == 2:
                print('1) Easy (max word lenght 4 & trys = 10)')
                print('2) Normal (max word lenght 6 & trys = 7)')
                print('3) Hard (max word lenght 10 trys = 5)')
                print('4) Insane (max word lenght 100 trys = 2)')
                print('5) Back')
                diff_select = input('->')
                if diff_select.isdigit():
                    diff_select = int(diff_select)
                    if diff_select == 5:
                        continue
                    elif diff_select == 1:
                        word_lenght = 4
                        trys = 10
                    elif diff_select == 2:
                        word_lenght = 6
                        trys = 7
                    elif diff_select == 3:
                        word_lenght = 10
                        trys = 5
                    elif diff_select == 4:
                        word_lenght = 100
                        trys = 2
                    else:
                        print('Sorry, thats not a valid selection')
                else:
                    print('Sorry, thats not a valid input')
            else:
                print('Sorry, thats not a valid selection')
        else:
            print('Sorry, thats not a valid input')


menu()