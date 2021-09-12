import random
pointarr = []
def init(x,y):
    boxCount = 3
    distx = x/boxCount
    disty = y/boxCount
    for y in range(boxCount):
        for x in range(boxCount):
            pointarr.append((random.randrange(distx * x, distx * (x+1),1),random.randrange(disty * y, disty * (y+1),1)))
    print(pointarr)
    return pointarr






def update(rectobj):
    #print(rectobj.center)
    x = rectobj.centerx


    rectobj.update(random.choice(pointarr),rectobj.size)

    return rectobj
