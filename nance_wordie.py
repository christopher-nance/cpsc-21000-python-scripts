#title           :nance_wordie.py
#description     :Game of Wordle.
#author          :Chris Nance
#date            :2022-03-16
#version         :1.0
#usage           :python nance_wordie.py
#notes           :
#python_version  :3.10
#==============================================================================#


## LIBRARIES
from random import randint


## VARIABLES
wordlist_file = (r"Test Objects\words.txt")
wordlist = []
guesses = 0
keepPlaying = 'Y'
wordToGuess = ''

## LISTS
previousGuesses = [] # // with below


## FUNCTIONS
def printGameBoard():
    print("Printing game board...")
    for item in previousGuesses: print("{: >5} {: >5} {: >5} {: >5} {: >5}".format(*item)) # https://docs.python.org/2.7/library/string.html#format-specification-mini-language
    

## SETUP
# Import all words into a single list.
for line in open(wordlist_file, 'r'):
    wordlist.append(line.strip())


## MAIN | *=good X=bad ~=wrong spot
print('''
***************************************************************************
                                   WORDIE
***************************************************************************


Welcome to WORDIE, the game everyone is playing. Your job is to guess
a five-letter word. You start with a completely blank set of five letter
tiles. As you guess a letter that is in the word, it will appear, either
out of place, in which case it will be marked with a ~ symbol, or in its
proper place, where it will be marked with a * symbol. Letters that are
out of place will be marked with an X symbol. The fewer tries it takes you 
to get all the letters in the right place, the faster you will guess the 
entire word. Only guesses that are actually words in the word list will be 
accepted. 

Good luck!

''')
while keepPlaying.lower() == 'y':
    print('\n'*20)
    print("Playing")
    previousGuesses.clear()
    wordToGuess = wordlist[randint(0, len(wordlist)-1)].lower()
    while guesses < 6:
#        print("WORD TO GUESS:", wordToGuess)
        printGameBoard()
        guess = input("Enter your guess: ").lower()
        guesses += 1
        if guess in wordlist:
            # Player's Guess was a word in the list.
            guessToAppend = []
            guessSymbolsToAppend = []
            for index, character in enumerate(guess):
                if character == wordToGuess[index]:
                    # Good character in correct spot.
                    guessToAppend.append((character))
                    guessSymbolsToAppend.append("*")
                elif character in wordToGuess.split():
                    # Bad placement of character.
                    guessToAppend.append((character))
                    guessSymbolsToAppend.append("~")
                else:
                    # Letter is not in the word.
                    guessToAppend.append((character))
                    guessSymbolsToAppend.append("x")
            # OUTPUT SETUP
            previousGuesses.append(guessSymbolsToAppend)
            previousGuesses.append(guessToAppend)
            previousGuesses.append(['','','','','']) # Place holder for spacing between guesses.
            
            if guess == wordToGuess: 
                print("Congrats! You guessed the word in less than 6 tries.")
                break
            print("You have", str(6-guesses), 'left.')
        else:
            # Player's Guess was NOT a word in the list.
            print("Sorry, that word is not in the word list. Try again. (No guesses were used)")
    print('\n'*2)
    keepPlaying = input("Press Y to keep playing or any other key to exit.")