data = open("./day6.txt").read().split(",")
print(data)
for _ in range(0, 256):
    print(i)
    newFish = 0
    for x, fish in enumerate(data): 
        if int(fish) == 0:
            data[x] = 6
            newFish+=1
        else: 
            data[x] = int(data[x]) - 1
    for z in range(0, newFish):
        data.append(8)
    #print("new day: ", data)
print(len(data))