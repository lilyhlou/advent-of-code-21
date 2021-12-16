import heapq

with open("./day15.txt") as file:
    data = [[int(d) for d in (line.strip())] for line in file]

    #part 2 
    coordinates = [[None for x in range(len(data)*5)] for y in range(len(data[0])*5)]
    for i in range(0,5):
        for z in range(0,5):
            for x, row in enumerate(data):
                for y, col in enumerate(row):
                        #print(coordinates[x+(len(data)*i)][y])
                        result = (int(data[x][y])+(1*i)+(1*z), int((data[x][y])+(1*i)+(1*z))%9)[(int(data[x][y])+(1*i)+(1*z)) > 9]
                        coordinates[x+(len(data)*i)][y+(len(data[0])*z)] = result #+ (1*z);  [y + (len(data[0] * z))]
    data = coordinates
    #end part 2
    

    visited = [[0 for x in range(len(data))] for y in range(len(data[0]))] #keeps track of distance from 0,0. is 0 by default
    visitedSet = set()
    q = [(0,0,0)]
    while q: 
        (d, x, y) = heapq.heappop(q)
        d += data[x][y]
        if (not (x == 0 and y == 0)) and (visited[x][y] == 0 or d < visited[x][y]):
            visited[x][y] = d
        if x == len(data)-1 and y == len(data[0])-1:
            break
        if x + 1 < len(data) and tuple([x+1,y]) not in visitedSet:
            visitedSet.add(tuple([x+1,y]))
            newPathLength = visited[x][y] + data[x+1][y]
            if not (visited[x+1][y] == 0):
                newPathLength = min(newPathLength, visited[x+1][y]) 
            visited[x+1][y] = newPathLength
            heapq.heappush(q, (newPathLength, x+1, y))
        if x - 1 >= 0 and tuple([x-1,y]) not in visitedSet:
            visitedSet.add(tuple([x-1,y]))
            newPathLength = visited[x][y] + data[x-1][y]
            if not visited[x-1][y] == 0:
                newPathLength = min(newPathLength, visited[x-1][y])
            visited[x-1][y] = newPathLength
            heapq.heappush(q, (newPathLength, x-1, y))
        if y + 1 < len(data[0]) and tuple([x,y+1]) not in visitedSet:
            visitedSet.add(tuple([x,y+1]))
            newPathLength = visited[x][y] + data[x][y+1]
            if not visited[x][y+1] == 0:
                newPathLength = min(newPathLength, visited[x][y+1])
            visited[x][y+1] = newPathLength
            heapq.heappush(q, (newPathLength, x, y+1))
        if y - 1 >= 0 and tuple([x,y-1]) not in visitedSet:
            visitedSet.add(tuple([x,y-1]))
            newPathLength = visited[x][y] + data[x][y-1]
            if not visited[x][y-1] == 0:
                newPathLength = min(newPathLength, visited[x][y-1])
            visited[x][y-1] = newPathLength 
            heapq.heappush(q, (newPathLength, x, y-1))
    print(visited[-1][-1])