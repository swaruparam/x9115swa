from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def position(t, n):
    pu(t)
    fd(t,n)
    pd(t)
    
def draw(t, n, r):
    angle = 360.0/n
    isos_angle = (180-angle)/2
    length_squared = 2*(1-math.cos(math.radians(angle)))*(r**2)
    length = math.sqrt(length_squared)
    for i in range(n):
        fd(t, r)
        lt(t, 180-isos_angle)
        fd(t, length)
        lt(t, 180-isos_angle)
        fd(t, r)
        rt(t, 180)    
 
# First pie
position(bob, -100)
draw(bob, 5, 60)

# Second pie
position(bob, 200)
draw(bob, 6, 60)

# Third pie
position(bob, 200)
draw(bob, 7, 60)


wait_for_user()
