import random
import math
import pygame
pointarr = []
goal = [0,0] #initialize arbitrary list
speedconst = .75

def init(x,y):
    boxCount = 3
    distx = x/boxCount
    disty = y/boxCount
    for y in range(boxCount):
        for x in range(boxCount):
            pointarr.append((random.randrange(distx * x, distx * (x+1),1),random.randrange(disty * y, disty * (y+1),1)))
    print(pointarr)
    return pointarr


#This function needs to be made better, but im really tired and cba
def findClosest(goal,revbox):#probably is called too much and is making some slowdown, o wellllll
    oldClosest = 10000 #incredibly arbitrary
    closestArrVal = 0
    closestTo = 10000
    for i,x in enumerate(pointarr):
        closestTo = min(closestTo,abs(math.sqrt((x[0] - revbox.centerx)**2+(x[1] - revbox.centery)**2)))
        if closestTo < oldClosest:
            closestArrVal = i
            oldClosest = closestTo
    if(pointarr[closestArrVal] == goal):
        print("caught ya")
        print(str(revbox.center) + " " + str(goal))
        return list(revbox.center)
    return goal

def checkGoal(tupleXY,goal):
    if abs( goal[0]- list(tupleXY)[0]) <=5 and abs(goal[1] - list(tupleXY)[1]) <=5:
        return True
    return False

def update(rectobj,goal,revbox):
    #print(rectobj.center)
    x = rectobj.centerx
    goal = findClosest(goal,revbox)
    if checkGoal(rectobj.center,goal):
        goal = random.choice(pointarr)
        pygame.time.wait(500)
    else:
        mag = abs(math.sqrt((goal[0] - rectobj.centerx) ** 2 + (goal[1] - rectobj.centery) ** 2))
        rectobj.move_ip(round(speedconst * ((goal[0] - rectobj.centerx)/mag)), round(speedconst * ((goal[1] - rectobj.centery)/mag)))
    return rectobj,goal

def RevUpdate(revbox,revboxVal):
    if revboxVal:
        revbox.center = pygame.mouse.get_pos()
    return revbox
        

