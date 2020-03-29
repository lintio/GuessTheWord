import random, os, sys
from words import word_list as wordList
feedback = ''
winLose = ''

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

def selectWord(wordlength, lastWord):
    #select a new word from word list and change to upper case
    newWord = random.choice(wordList).upper()
    if newWord == lastWord:
        newWord = random.choice(wordList).upper()
    else:
        while len(newWord) > wordlength:
            newWord = random.choice(wordList).upper()
    return(newWord)

def play(currentWord, level, wordlength):
    #init vers
    global feedback
    global winLose
    activeWord = currentWord
    guessedLetters = []
    guessedWords = []
    attempts = level
    wordCompletion = '_' * len(activeWord)
    guessed = False
    while guessed == False:
        #check for lose
        if attempts <= 0 and guessed == False:
            winLose = 'lose'
            feedback = 'sorry you lost the word was ' + activeWord
            menu()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(activeWord) #see word for testing
            print('Guessed letters -', guessedLetters, 'Guessed Words -', guessedWords)
            print(hangman[attempts])
            print('\n')
            print(wordCompletion)
            print(feedback)
            guess = input('->').upper()
            #check input is a string
            if guess.isalpha():
                
                #check if input is a letter or word
                #checks if letter
                if len(guess) == 1:
                    if guess not in guessedLetters and guess not in activeWord:
                        guessedLetters.append(guess)
                        attempts -= 1
                        feedback = 'Sorry that letter is not in the word'
                    elif guess in guessedLetters:
                        feedback = 'you have already guessed ' + guess
                    else:
                        guessedLetters.append(guess)
                        #find index of letter in activeWord
                        for x, letter in enumerate(activeWord):
                            if guess == letter:
                                wordCompletion = list(wordCompletion)
                                wordCompletion[x] = letter
                                wordCompletion = ''.join(wordCompletion)
                        feedback = ''
                        if wordCompletion == activeWord:
                            feedback = 'Well done you guessed the word! ' + activeWord
                            winLose = 'win'
                            guessed = True
                #checks if the guess is the length of activeWord
                elif len(guess) == len(activeWord):
                    if guess not in guessedWords and guess != activeWord:
                        guessedWords.append(guess)
                        attempts -= 1
                        feedback = 'Sorry, ' + guess + ' is not the word'
                    elif guess in guessedWords:
                        feedback = 'You have already guessed ' + guess
                    else:
                        feedback = 'Well done you guessed the word! ' + activeWord
                        winLose = 'win'
                        guessed = True
                else:
                    feedback = 'Sorry that is not a valid guess'

def menu():
    global feedback
    global winLose
    menuSelect = 5
    wordlength = 10
    level = 5
    lastWord = ''
    while menuSelect != 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        if winLose == 'lose':
            print("""
    /---\\
    |   |
    |   o
    |  /|\\   Sorry, You Lost
    |  / \\
    |
   / \\____
   """)
        elif winLose == 'win':
            print("""
    \\o/
     |    Congratulations!!
    / \\
            """)
        print(feedback)
        print('Current settings - Max Word length =', wordlength, ' & tries =', level, '-')
        print('1) Play')
        print('2) Change Settings')
        print('3) Quit')
        menuSelect = input('->')
        if menuSelect.isdigit:
            menuSelect = int(menuSelect)
            if menuSelect == 3:
                exit()
            elif menuSelect == 1: #Play
                newWord = selectWord(wordlength, lastWord)
                lastWord = newWord
                feedback = ''
                play(newWord, level, wordlength)
            elif menuSelect == 2: #Settings
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Current settings - Max Word length =', wordlength, ' & tries =', level, '-')
                print('1) Easy (max word length 4 & tries = 10)')
                print('2) Normal (max word length 6 & tries = 7)')
                print('3) Hard (max word length 10 tries = 5)')
                print('4) Insane (max word length 100 tries = 2)')
                print('5) Back')
                diffSelect = input('->')
                if diffSelect.isdigit():
                    diffSelect = int(diffSelect)
                    if diffSelect == 5:
                        continue
                    elif diffSelect == 1:
                        wordlength = 4
                        level = 10
                    elif diffSelect == 2:
                        wordlength = 6
                        level = 7
                    elif diffSelect == 3:
                        wordlength = 10
                        level = 5
                    elif diffSelect == 4:
                        wordlength = 100
                        level = 2
                    else:
                        print('Sorry, thats not a valid selection')
                else:
                    print('Sorry, thats not a valid input')
            else:
                print('Sorry, thats not a valid input')
        else:
            print('Sorry, thats not a valid input')

menu()