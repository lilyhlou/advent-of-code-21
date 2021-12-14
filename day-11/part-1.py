def lightup(data, lights):
    count = 0
    for light in lights:
        [x,y] = light
        if y-1 >= 0:
            if data[x][y - 1] == 9:
                data[x][y - 1] = 0
                count+=1
                lights.append(tuple([x, y-1]))
            elif not data[x][y-1] == 0:
                data[x][y - 1]+=1
            if x-1 >= 0:
                if data[x-1][y - 1] == 9:
                    data[x-1][y - 1] = 0
                    count+=1
                    lights.append(tuple([x-1, y-1]))
                elif not data[x-1][y - 1] == 0:
                    data[x-1][y - 1] +=1
            if x+1 < len(data):
                if data[x+1][y - 1] == 9:
                    data[x+1][y - 1] = 0
                    count+=1
                    lights.append(tuple([x+1, y-1]))
                elif not data[x+1][y - 1] == 0:
                    data[x+1][y - 1] +=1
        if x-1 >=0: 
            if data[x-1][y] == 9:
                data[x-1][y] = 0
                count+=1
                lights.append(tuple([x-1, y]))
            elif not data[x-1][y] == 0:
                data[x-1][y]+=1
        if x+1 < len(data): 
            if data[x+1][y] == 9:
                data[x+1][y] = 0
                count+=1
                lights.append(tuple([x+1, y]))
            elif not data[x+1][y] == 0:
                data[x+1][y] +=1
        if y+1 < len(data[0]):
            if data[x][y+1] == 9:
                data[x][y+1] = 0
                count+=1
                lights.append(tuple([x, y+1]))
            elif not data[x][y + 1] == 0:
                data[x][y+1] += 1
            if x-1 >= 0:
                if data[x-1][y+1] == 9:
                    data[x-1][y+1] = 0
                    count+=1
                    lights.append(tuple([x-1, y+1]))
                elif not data[x-1][y+1] == 0:
                    data[x-1][y+1]+=1
            if x+1 < len(data):
                if data[x+1][y+1] == 9:
                    data[x+1][y+1] = 0
                    count+=1
                    lights.append(tuple([x+1, y+1]))
                elif not data[x+1][y+1] == 0:
                    data[x+1][y+1]+=1
    return count
  
with open("./day11.txt") as file:
    data = [[int(d) for d in (line.strip())] for line in file]
    lights = []
    lightCount = 0
    allFlash = [[0]*10]*10     # part 2 
    i=0 #part 2
    while not allFlash == data: # part 2 otherwise for x in range(0,100)
        for x, col in enumerate(data):
            for y, row in enumerate(col):
                if data[x][y] == 9:
                    lights.append(tuple([x,y]))
                    lightCount+=1
                    data[x][y] = 0
                else:
                    data[x][y] += 1
        i+=1
        print("i", i) #answer to pt 2
        lightCount += lightup(data, lights)
        lights = []
    print(lightCount) #part 1 