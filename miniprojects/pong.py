# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [HALF_WIDTH, HALF_HEIGHT]
    ball_vel = [1, 1]
    
    fps = 60 # Frames p/ Second
    x = random.randrange(120, 240) / fps # horizontal
    y = random.randrange(60, 180)  / fps # vertical
    
    if direction == RIGHT:
        ball_vel = [x, -y]
    else:
        ball_vel = [-x, -y]

def reflect_ball():
    global ball_vel
    ball_vel[1] += ball_vel[1] * 0.1
    ball_vel[0] += ball_vel[0] * 0.1
    ball_vel[0] = - ball_vel[0] # reflect

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = [HALF_PAD_WIDTH, HALF_HEIGHT]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HALF_HEIGHT]
    
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    
    score1 = 0
    score2 = 0
    
    spawn_ball(random.choice([1, 2]))

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White") # Mid Line
    c.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White") # Left Gutter
    c.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White") # Right Gutter
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    
    # collide and reflect off of top hand side of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] =- ball_vel[1]
    # collide and reflect off of botton hand side of canvas
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] =- ball_vel[1]
       
    # collide with the left gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT  \
            and ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            reflect_ball()
        else:
            score2 += 1
            spawn_ball(RIGHT)
    # collide with the right gutter
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT  \
            and ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            reflect_ball()
        else:
            score1 += 1
            spawn_ball(LEFT)

    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Blue", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    tmp = paddle1_pos[1] + paddle1_vel[1]
    if tmp <= HEIGHT - HALF_PAD_HEIGHT and tmp >= HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel[1]
    tmp = paddle2_pos[1] + paddle2_vel[1]
    if tmp <= HEIGHT - HALF_PAD_HEIGHT and tmp >= HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel[1]        

    # draw paddles
    c.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT],
                [paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT],
                PAD_WIDTH, "White") # Left Paddle
    c.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT],
                [paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT],
                PAD_WIDTH, "White") # Right Paddle
    
    # draw scores
    c.draw_text(str(score1), ((HALF_WIDTH // 2) - PAD_WIDTH, 40), 30, 'White')
    c.draw_text(str(score2), ((WIDTH + HALF_WIDTH + PAD_WIDTH) / 2, 40), 30, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 8
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -acc
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["s"] or key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0        

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game, 100)


# start frame
new_game()
frame.start()
