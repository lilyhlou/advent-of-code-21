#target area: x=230..283, y=-107..-57
xmin = 230
xmax = 283
ymin = -107
ymax = -57
def inTargetRange(x,y):
    if x< xmin or x>xmax or y < ymin or y > ymax:
        return False
    return True

count = 0
xstartvelocity = 0
while xstartvelocity <= xmax:
    ystartvelocity = ymin
    while ystartvelocity < abs(ymin):
        x = 0 
        y = 0
        xvelocity = xstartvelocity
        yvelocity = ystartvelocity
        while y > ymin:
            x+=xvelocity
            y+=yvelocity
            if inTargetRange(x,y):
                count+=1
                break
            yvelocity-=1
            if xvelocity > 0:
                xvelocity-=1
            elif xvelocity < 0:
                xvelocity+=1
        ystartvelocity+=1
    xstartvelocity+=1
print(count)