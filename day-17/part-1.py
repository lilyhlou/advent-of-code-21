#target area: x=230..283, y=-107..-57
def inTargetRange(x,y):
    if x< 230 or x>283 or y < -107 or y > -57:
        return False
    return True

maxHeight = 0
xstartvelocity = 0
while xstartvelocity < 283:
    ystartvelocity = -107
    while ystartvelocity < 107:
        x = 0 
        y = 0
        xvelocity = xstartvelocity
        yvelocity = ystartvelocity
        localMax = 0
        while y > -107:
            x+=xvelocity
            y+=yvelocity
            if y > localMax:
                localMax = y
            if inTargetRange(x,y):
                if maxHeight < localMax:
                    maxHeight = localMax
            yvelocity-=1
            if xvelocity > 0:
                xvelocity-=1
            elif xvelocity < 0:
                xvelocity+=1
        ystartvelocity+=1
    xstartvelocity+=1
print(maxHeight)
