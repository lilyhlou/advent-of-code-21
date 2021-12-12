with open("./day8.txt") as file:
    data = [line.strip().split("|")[1] for line in file]
    count = 0
    for line in data: 
        displays = line.strip().split()
        for display in displays: 
            length = len(display)
            if length in [2,3,4,7]:
                count+=1
    print(count)
