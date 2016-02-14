# template for "Stopwatch: The Game"

import simplegui

# define global variables
message = ''
score = tries = current_time = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    m = (t / 10) / 60
    s = (t / 10) % 60
    if s < 10:
        s = '0' + str(s)
    ms = t % 10
    return str(m) + ':' + str(s) + '.' + str(ms)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global is_running
    if not is_running:
        is_running = True
        timer.start()

def stop_handler():
    global tries, score, is_running
    if is_running:
        is_running = False
        timer.stop()
        tries = tries + 1
        ms = current_time % 10
        if ms == 0:
            score = score + 1
            
def reset_handler():
    global current_time, score, tries
    global is_running, message
    if is_running:
        is_running = False
        timer.stop();
    score = tries = current_time = 0
    message = format(current_time)
    
            
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global current_time
    current_time = current_time + 1    

# define draw handler
def draw_handler(canvas):
    global message
    message = format(current_time)
    scores = str(score) + '/' + str(tries)
    canvas.draw_text(scores, (250, 20), 20, 'Green')
    canvas.draw_text(message, (110, 110), 30, 'White')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_handler, 200)
frame.add_button('Stop', stop_handler, 200)
frame.add_button('Reset', reset_handler, 200)

# start frame
frame.start()

# Please remember to review the grading rubric
