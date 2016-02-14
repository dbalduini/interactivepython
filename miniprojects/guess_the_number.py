# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random, math

# initialize global variables used in your code
num_range = 100
secret_num = 0
num_guesses = 0

# helper function to start and restart the game
def new_game():
    """
        Start a new game.
        Use binary search algorithm to determine the 
        number of possible guesses. (2 ** n >= high - low + 1)
        
        see: http://en.wikipedia.org/wiki/Binary_search_algorithm
    """
    global secret_num, num_guesses
    print 'New game. Range is from 0 to', num_range
    # Generate a secret number
    secret_num = random.randrange(0, num_range)
    # Calculate the number of possible guesses
    num_guesses = int(math.ceil(math.log(num_range,2)))
    print 'Number of remaining guesses is', num_guesses
    print
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000 
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global num_guesses
    print 'Guess was', guess
    num_guesses = num_guesses - 1;
    print 'Number of remaining guesses is', num_guesses
    guess = int(guess)
    if guess == secret_num:
        print 'Correct!\n'
        new_game()
    elif num_guesses == 0:
        print 'You run out of guesses. The number was', secret_num, '\n'
        new_game()
    elif secret_num < guess :
        print 'Lower\n'
    else:
        print 'Highter\n'

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)",range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
