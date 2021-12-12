with open("./day5.txt") as file:
    data = [line.strip() for line in file]
    oceanFloorMap = {} #use dictionary because unknown far many points to use
    countOverlap = 0
    for line in data:
        points = line.split("->")
        lineCords = []
        for point in points: 
            cord = [x.strip() for x in point.split(',')]
            lineCords.append(cord)
        if lineCords[0][0] == lineCords[1][0]: #x axis is same, horizonal line
            start = (lineCords[1][1], lineCords[0][1])[int(lineCords[0][1]) < int(lineCords[1][1])] #y value
            end = (lineCords[0][1], lineCords[1][1])[int(lineCords[0][1]) < int(lineCords[1][1])]
            for y in range(int(start), int(end)+1):
                if (int(lineCords[0][0]), y) in oceanFloorMap:
                    oceanFloorMap[int(lineCords[0][0]), y] = oceanFloorMap[int(lineCords[0][0]), y] + 1
                    if(oceanFloorMap[int(lineCords[0][0]), y] == 2):
                        countOverlap+=1
                else: 
                    oceanFloorMap[int(lineCords[0][0]), y] = 1
        if lineCords[0][1] == lineCords[1][1]: #y axis is same
            start = (lineCords[1][0], lineCords[0][0])[int(lineCords[0][0]) < int(lineCords[1][0])] #y value
            end = (lineCords[0][0], lineCords[1][0])[int(lineCords[0][0]) < int(lineCords[1][0])]
            for x in range(int(start), int(end)+1):
                if (x, int(lineCords[0][1])) in oceanFloorMap:
                    oceanFloorMap[x, int(lineCords[0][1])] = oceanFloorMap[x, int(lineCords[0][1])] + 1
                    if(oceanFloorMap[x, int(lineCords[0][1])] == 2):
                        countOverlap+=1
                else: 
                    oceanFloorMap[x, int(lineCords[0][1])] = 1
    print(countOverlap)            