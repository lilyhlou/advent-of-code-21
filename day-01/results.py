with open("./day1.txt") as file:
    data = [int(line.strip()) for line in file]

    #part 1
    prev = data[0]
    increasesCount = 0
    for number in data: 
        if number > prev: 
            increasesCount+=1
        prev = number
    print(increasesCount)

    #part 2
    window = data[:3] #keep max 3 values
    prevSum = sum(window)
    sumIncreases = 0
    for i in range(3, len(data)):
        window.pop(0)
        window.append(data[i])
        currSum = sum(window)
        if currSum > prevSum:
            sumIncreases+=1
        prevSum = currSum
    print(sumIncreases)



