def findBasin(map, x, y, visited):
    q = [tuple([x,y])] #queue to visit
    size = 0
    visited[x][y] = True
    while len(q) > 0:
        [x,y] = q.pop()
        size+=1 
        if y-1 >= 0:
            if not data[x][y - 1] == 9 and not visited[x][y - 1]:
                q.append(tuple([x,y-1]))
                visited[x][y-1] = True
        if y + 1 < len(map[0]):
            if not data[x][y + 1] == 9 and not visited[x][y+1]:
                q.append(tuple([x,y+1]))
                visited[x][y+1] = True
        if x - 1 >= 0:
            if not data[x-1][y] == 9 and not visited[x-1][y]:
                q.append(tuple([x-1,y]))
                visited[x-1][y] = True
        if x+1 < len(map):
            if not data[x+1][y] == 9 and not visited[x+1][y]:
                q.append(tuple([x+1,y]))
                visited[x+1][y] = True
    return size

with open("./day9.txt") as file:
    data = [[int(d) for d in (line.strip())] for line in file]
    riskLevel = 0
    visited = []
    basinSizes = []
    while len(visited) < len(data):
        column = []
        while len(column) < len(data[0]):
            column.append(False)
        visited.append(column)
    for x, row in enumerate(data):
        for y, numVal in enumerate(row):
            smallest = True
            if y-1 >= 0:
                if data[x][y - 1] <= numVal:
                   smallest = False
            if y + 1 < len(row) and smallest:
                if data[x][y + 1] <= numVal:
                   smallest = False
            if x - 1 >= 0 and smallest:
                if data[x-1][y] <= numVal:
                   smallest = False
            if x+1 < len(data) and smallest:
                if data[x+1][y] <= numVal:
                   smallest = False
            if smallest:
                smallest= False
                basinSizes.append(findBasin(data, x, y, visited))
    basinProduct = 1
    for basinSize in sorted(basinSizes)[-3:]:
        basinProduct = basinSize * basinProduct
    print(basinProduct)