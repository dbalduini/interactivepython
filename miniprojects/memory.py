# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global memory_deck, exposed, state, turn
    
    # Create the memory deck
    memory_deck = range(0, 8) * 2
    random.shuffle(memory_deck)

    # Init globals
    exposed = [False] * 16
    state = turn = 0

# define event handlers
def mouseclick(pos):
    global state, idx_1, idx_2, turn

    idx = pos[0] / 50
    if not exposed[idx]:
        exposed[idx] = True
        if state == 0:
            idx_1 = idx
            state = 1
        elif state == 1:
            idx_2 = idx
            state = 2
            turn = turn + 1
        else:
            if memory_deck[idx_1] != memory_deck[idx_2]:
                exposed[idx_1] = False
                exposed[idx_2] = False
            state = 1
            idx_1 = idx

# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " + str(turn))
    pos = 0
    for idx in range(len(memory_deck)):
        if exposed[idx]:
            n = memory_deck[idx]
            canvas.draw_text(str(n), (pos+10, 50+15), 50, "White")
        else:
            canvas.draw_polygon([(pos, 0), (pos, 100), (pos+50, 100), (pos+50, 0)], 3, 'Grey', 'Green')
        pos = pos + 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric