
import sys

vel = 0

# Friction
def update():
    global vel
    vel += 10 # Acceleration
    vel *= .9 # 10% of the velocity
    
def simulate(n):
    for i in range(n):
        update()
        print vel 
        
simulate(int(sys.argv[1]))

