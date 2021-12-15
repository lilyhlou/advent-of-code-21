inputs = open("./day13.txt").read().split("\n\n")
coordinates = inputs[0].split()
instructions = inputs[1].split("\n")
for i, instruction in enumerate(instructions):
    instructions[i] = instruction.split()[2].split('=')
for instruction in instructions:
    afterFold = []
    for coordinate in coordinates:
        if instruction[0] == 'y':
            coordinateValue = coordinate.split(',')
            newYValue = int(instruction[1]) - abs(int(instruction[1])-int(coordinateValue[1]))
            afterFold.append(str(coordinateValue[0])+","+str(newYValue))
        if instruction[0] == 'x':
            coordinateValue = coordinate.split(',')
            newXValue = int(instruction[1]) - abs(int(instruction[1])-int(coordinateValue[0]))
            afterFold.append(str(newXValue)+","+str(coordinateValue[1]))
    coordinates = set(afterFold)

array = [ ['.'] * 10 for i in range(40) ]
for coord in coordinates:
    x, y = coord.split(',')
    array[int(x)][int(y)] = '#'
for row in array:
    print(row, '\n')