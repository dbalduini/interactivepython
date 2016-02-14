# Ball motion with an explicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [3, 0.7]  # pixels per tick
time = 0

# define event handlers
def tick():
    global time
    time = time + 1

def draw(canvas):
    # create a list to hold ball position
    ball_pos = [10, 20]

    # calculate ball position
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[1] + time * vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # draw rectangle
    canvas.draw_polygon([(50, 50), (180, 50), (180, 140), (50, 140)], 12, 'Red')

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(50, tick)

# start frame
frame.start()
timer.start()
