with open("./day9.txt") as file:
    data = [[int(d) for d in (line.strip())] for line in file]
    riskLevel = 0
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
                riskLevel+= numVal + 1
    print(riskLevel)
        




            


