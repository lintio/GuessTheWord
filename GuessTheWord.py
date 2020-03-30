import random, os, sys
from words import word_list as wordList
feedback = ''
winLose = ''

class settings:
    wordlength = 10
    level = 2
    attempts = 5


hangman = ["""
    /---\\
    |   |
    |   o
    |  /|\\   Hangman!
    |  / \\
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |  /|\\   Hangman
    |  / 
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |  /|\\   Hangma
    |  
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |  /|    Hangm
    |
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |   |    Hang
    |  
    |
   / \\____
   """,
   """
    /---\\
    |   |
    |   o
    |        Han
    |  
    |
   / \\____
   """,
   """
    /---\\
    |   
    |   
    |        Ha
    |  
    |
   / \\____
   """,
   """
    /
    |   
    |   
    |        H
    |  
    |
   / \\____
   """,
   """
    
       
       
      
    |  
    |
   / \\____
   """,
   """
    
       
       
    
      
    
   / \\____
   """,
   """
    
       
       Let's Play Hangman!
     Guess Letters and Words  
    Words to save the Hangman!
        
   _______
   """]

def selectWord(lastWord):
    #select a new word from word list and change to upper case
    newWord = random.choice(wordList).upper()
    if newWord == lastWord:
        newWord = random.choice(wordList).upper()
    else:
        while len(newWord) > settings.wordlength:
            newWord = random.choice(wordList).upper()
    return(newWord)

def play(currentWord):
    #init vers
    global feedback
    global winLose
    activeWord = currentWord
    guessedLetters = []
    guessedWords = []
    attempts = 10
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
           # print(activeWord) #see word for testing
            print('Guessed letters -', guessedLetters, 'Guessed Words -', guessedWords)
            if attempts <= 0:
                print(hangman[0])
            else:
                print(hangman[attempts])
            print('\n')
            print('-> ' + wordCompletion + ' <-')
            print(feedback)
            guess = input('->').upper()
            #check input is a string
            if guess.isalpha():
                
                #check if input is a letter or word
                #checks if letter
                if len(guess) == 1:
                    if guess not in guessedLetters and guess not in activeWord:
                        guessedLetters.append(guess)
                        attempts -= settings.level
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
                        attempts -= settings.level
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
        else:
            print("""
    /---\\
    |   |
    |   o
    |  /|\\   Hangman
    |  / \\
    |
   / \\____
   """)
        print(feedback)
        print('Current settings - Max Word length =', settings.wordlength, '& tries =', settings.attempts, '-')
        print('1) Play')
        print('2) Change Settings')
        print('3) Quit')
        menuSelect = input('->')
        if menuSelect.isdigit:
            menuSelect = int(menuSelect)
            if menuSelect == 3:
                exit()
            elif menuSelect == 1: #Play
                newWord = selectWord(lastWord)
                lastWord = newWord
                feedback = ''
                play(newWord)
            elif menuSelect == 2: #Settings
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Current settings - Max Word length =', settings.wordlength, '& tries =', settings.attempts, '-')
                print('1) Easy (max word length 4 & tries = 10)')
                print('2) Normal (max word length 6 & tries = 5)')
                print('3) Hard (max word length 10 tries = 3)')
                print('4) Insane (max word length 100 tries = 2)')
                print('5) Back')
                diffSelect = input('->')
                if diffSelect.isdigit():
                    diffSelect = int(diffSelect)
                    if diffSelect == 5:
                        continue
                    elif diffSelect == 1:
                        settings.wordlength = 4
                        settings.level = 1
                        settings.attempts = 10
                    elif diffSelect == 2:
                        settings.wordlength = 6
                        settings.level = 2
                        settings.attempts = 5
                    elif diffSelect == 3:
                        settings.wordlength = 10
                        settings.level = 4
                        settings.attempts = 3 
                    elif diffSelect == 4:
                        settings.wordlength = 100
                        settings.level = 5
                        settings.attempts = 2
                    else:
                        print('Sorry, thats not a valid selection')
                else:
                    print('Sorry, thats not a valid input')
            else:
                print('Sorry, thats not a valid input')
        else:
            print('Sorry, thats not a valid input')

menu()