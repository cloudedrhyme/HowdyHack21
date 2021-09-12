


def update(rectobj):
    print(rectobj.center)
    x = rectobj.centerx
    if(x-60):
        x = -5
    else:
        x=5
    
    rectobj = rectobj.move(x,0)

    return rectobj