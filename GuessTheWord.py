import random, os
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
    new_word = random.choice(word_list).upper()
    while len(new_word) > word_lenght:
        new_word = random.choice(word_list).upper()
    return(new_word)

def play(word, level, word_lenght):
    #setting up veriabled for later use
    currentWord = word
    guessed_letters = []
    guessed_words = []
    #lives = level
    attempts = level
    word_completion = '_' * len(currentWord)
    guessed = False
    response = ''
    #loop until guessed is true or attempts = 0
    while guessed == False:

        # This section is not working correctly or it could be the play again option not updating the word

        if attempts == 0 and guessed == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(currentWord)
            print('letters guessed ', guessed_letters)
            print('words guessed ', guessed_words)
            print(hangman[attempts])
            print('\n')
            print(word_completion)
            print('sorry you lost the word was', currentWord)
            try_again = input('Would you like to play again (Y/N) ->')
            try_again = try_again.upper()
            if try_again == 'Y':
                #seems to not reset the word for this bit
                guessed_letters = []
                guessed_words = []
                word_completion = '_' * len(currentWord)
                guessed = False
                menu(1)
            if try_again == 'N':
                break
            else:
                response = 'not a valid input'
        else:
            #quick and dirty output to see if it is working
            os.system('cls' if os.name == 'nt' else 'clear')
            print(currentWord)
            print('letters guessed ', guessed_letters)
            print('words guessed ', guessed_words)
            print(hangman[attempts])
            print('\n')
            print(word_completion)
            print(response)
            #take the users input and makes it upper case
            guess = input('->').upper()
            if guess.isalpha():
                #checks to see if its a letter
                if len(guess) == 1:
                    #check to see if it is in the guessed_letters array and the word
                    if guess not in guessed_letters and guess not in currentWord:
                        guessed_letters.append(guess)
                        attempts -= 1
                        response = 'sorry that letter is not in the word'
                    elif guess in guessed_letters:
                        response = 'you have already guessed the letter', guess
                    else:
                        guessed_letters.append(guess)
                        #checks if the letter is in the word by converting the word to a list and then back again
                        for x, letter in enumerate(currentWord):
                            if guess == letter:
                                word_completion = list(word_completion)
                                word_completion[x] = letter
                                word_completion = ''.join(word_completion)
                        #checks to see if all letters have been guessed works to start with
                        if word_completion == currentWord:
                            guessed = True
                            response = 'Well done You guessed the word!', currentWord
                #allows the player to guess the word as a whole
                elif len(guess) == len(word):
                    if guess not in guessed_words and guess != currentWord:
                        guessed_words.append(guess)
                        attempts -= 1
                        response = 'Sorry, That is not the word'
                    elif guess in guessed_words:
                        response = 'Sorry, You have already guessed', guess
                    else:
                        response = 'Well done You guessed the word!', currentWord
                        guessed_letters = []
                        guessed_words = []
                        word_completion = '_' * len(currentWord)
                        guessed = True
                else:
                    response = 'Sorry, thats not a valid input'
    return(guessed)

def menu(option, word):
    menu_select = option
    word_lenght = 10
    trys = 5
    guessed = False
    word = word
    if menu_select == 1:
        word = selectWord(word_lenght)
        guessed = play(word, trys, word_lenght)
    else:
        while menu_select != 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Current settings - Max Word Lenght =', word_lenght, ' & trys =', trys, '-')
            if guessed == True:
                print('Congradulations you won!!')
            elif guessed == False:
                print('Better luck next time. The last word was', word)
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
                    guessed = play(word, trys, word_lenght)
                elif menu_select == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Current settings - Max Word Lenght =', word_lenght, ' & trys =', trys, '-')
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


menu(5)