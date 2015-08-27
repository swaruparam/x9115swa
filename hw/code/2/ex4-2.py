from swampy.TurtleWorld import *     
def square(turtleParam, length):
    '''
     This module draws a square
    '''


    for i in range(4):
        fd(turtleParam, length)
        # fd means take 100 steps forward 
        # lt means turn left
        lt(turtleParam)

##        


def polygon(turtleParam, length, n ):
    '''
     This module draws a python
    '''

    for i in range(n):
        fd(turtleParam, length)
        # fd means take 100 steps forward 
        # lt means turn left
        degreeVal = 360 / n 
        lt(turtleParam, degreeVal)

##        


def circle(turtleParam, r ):
    import math
    '''
     This module draws a circle
    '''

    numOfSides = 90
    #num of sides must be larger to make a smoother circle 
    turtleParam.delay =  0.01     
    valToUse = math.pi / float (numOfSides) 
    lenOfPoly = 2 * r * math.sin(valToUse) 
    polygon(turtleParam, lenOfPoly ,numOfSides)

##        

def arc(turtleParam, r, angle):
    import math
    '''
     This module draws an arc
    '''    
    turtleParam.delay =  0.01     
    arclen = 2 * math.pi * r * angle / 360
    n = int(arclen / 3) + 1
    steplen = arclen / n
    stepangle = float(angle) / n
    
    for i in range(n):
        fd(turtleParam, steplen)
        lt(turtleParam, stepangle)

def drawPetal(tObj, rParam, angleParam):
    for i in range(2):
        arc(tObj, rParam, angleParam)
        lt(tObj, 180 - angleVal) 
    
    
def drawFlower(turtleParam, angleParam, petalNoParam, rValParam):
    #rVal=80
    for i in range(0, petalNoParam):
        drawPetal(turtleParam, rValParam, angleParam)
        lt(turtleParam, float(360/petalNoParam))

##    


lengthVal = 80
degreeVal = 6

#square(turtleObj, lengthVal)    
#polygon(turtleObj, lengthVal, degreeVal)
#circle(turtleObj, rVal) 
#arc(turtleObj, rVal, angleVal)
#Picture # 1 
world = TurtleWorld()
turtleObj = Turtle()
rVal=80
angleVal = 90
petalCount=5
drawFlower(turtleObj, angleVal, petalCount, rVal)
#Picture # 2
world = TurtleWorld()
turtleObj = Turtle()
rVal=40
angleVal = 80
petalCount=10
drawFlower(turtleObj, angleVal, petalCount, rVal)
#Picture # 3
world = TurtleWorld()
turtleObj = Turtle()
rVal=140
angleVal = 20
petalCount=20
drawFlower(turtleObj, angleVal, petalCount, rVal)
#Picture # 4
world = TurtleWorld()
turtleObj = Turtle()
rVal=90
angleVal = 90
petalCount=10
drawFlower(turtleObj, angleVal, petalCount, rVal)
#Picture # 5
world = TurtleWorld()
turtleObj = Turtle()
rVal=100
angleVal = 45
petalCount=20
drawFlower(turtleObj, angleVal, petalCount, rVal)
#Picture # 6
world = TurtleWorld()
turtleObj = Turtle()
rVal=60
angleVal = 60
petalCount=5
drawFlower(turtleObj, angleVal, petalCount, rVal)
#drawFlower(90, 10)
#drawFlower(90, 7)
#drawFlower(90, 6)
wait_for_user()    