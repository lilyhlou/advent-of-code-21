data = open("./day6.txt").read().split(",")
fishDictionary = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0} #fill in a key for 0 in case it doesn't exist
for i, fishDays in enumerate(data):
    if int(fishDays) in fishDictionary:
        fishDictionary[int(fishDays)] += 1
for _ in range(0, 256):
    temp = fishDictionary[list(reversed(sorted(fishDictionary)))[0]]
    for fishBirthday in reversed(sorted(fishDictionary)):  
        if fishBirthday == 0:
            temp2 = fishDictionary[8] #grab number of fish with 8 days to later decrement to 7 days
            fishDictionary[8] = temp
            fishDictionary[6] += temp
            temp = temp2
        else:
            fishDictionary[fishBirthday-1], temp = temp, fishDictionary[fishBirthday-1]
count = 0
for fish in sorted(fishDictionary):
    count += int(fishDictionary[fish])
print(count)