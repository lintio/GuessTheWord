Project idea from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

Hangman

The Goal: Despite the name, the actual “hangman” part isn’t necessary. The main goal here is to create a sort of “guess the word” game. The user needs to be able to input letter guesses. A limit should also be set on how many guesses they can use. This means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. No need to get too fancy.) You will also need functions to check if the user has actually inputted a single letter, to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.
Concepts to keep in mind:

Random
Variables
Boolean
Input and Output
Integer
Char
String
Length
Print


Likely the most complex project on this list (well, depending on just how intense you went with the adventure text game), the Hangman project compiles the prior concepts and takes them a step further. Here, outcomes are not only determined based on user-inputted data, that data needs to be parsed through, compared, and then either accepted or rejected. If you want to take this project a step further, set up a hangman image that changes!

My working plan
--------------------------------
only 5 wrong guesses allowed before a lose wrong guesses left 5/5
add incorrect letters to a list to display as letters guessed
show the word as _ so the word HANGMAN would be displayed like this _ _ _ _ _ _ _ this will allow the player to see the lengh of the word

maybe add a difficulty setting allowing the player to select a difficulty and have multipul lists or have longer words


game would look like this
\/

Worng Guesses -> [B, C, D, ]
Wrong Guesses Left -> 2/5
_ A _ _ _ _ _
-> 