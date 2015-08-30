from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def position(t, n):
    pu(t)
    fd(t,n)
    pd(t)
    
def draw(t, n, r, overlap):
    if overlap:
        angle = 360/(n/2)
        for i in range(n):
            arc(t, r, angle)
            lt(t,180-angle)
            arc(t, r, angle)
            rt(t,180+(angle/2))
    else:
        angle = 360/n
        for i in range(n):
            arc(t, r, angle)
            lt(t,180-angle)
            arc(t, r, angle)
            rt(t,180)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

        

# First flower
position(bob, -100)
draw(bob, 7, 50, False)

# Second flower
position(bob, 200)
draw(bob,10, 40, True)

# Third flower
position(bob, 200)
draw(bob, 20, 150, False)


wait_for_user()
