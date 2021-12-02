with open("./day2.txt") as file:
    data = [line.strip() for line in file]
    forward = 0
    depth = 0
    part2depth = 0 #part2: replace depth in line above with aim, increment part2depth for depth
    for movement in data: 
        direction = movement.split()
        if direction[0] == 'forward': 
            forward+=int(direction[1])
            part2depth=part2depth + depth*int(direction[1]) #part 2
        else: 
            depth = (depth + int(direction[1]), depth - int(direction[1]))[direction[0] == 'up']
    print(part2depth*forward)
