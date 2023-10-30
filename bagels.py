import random
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, by Al Sweigart, a deductive logic game.
    By Al Sweigart
          
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is.  Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    bagels      No digit is correct.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess=''
            while len(guess)!=NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = imput('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of gueses.')
                print('The answer was {}.'.format(secretNum))

        print("Would you like to play the game again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")

def getSecretNum():
    return True

def getClues(guess, secretNum):
    return True

if __name__ == '__main__':
    main()