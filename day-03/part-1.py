with open("./day3.txt") as file:
    data = [line.strip() for line in file]
    ones = [0] * 12 #index is the total number of 1s in the list
    for numbers in data: 
        splitNums = [int(i) for i in str(numbers)]
        for i, num in enumerate(splitNums):
            if num == 1:
                ones[i] = ones[i] + 1
    gamma = ''
    epsilon = ''
    for count in ones:
        zeroes = len(data) - count
        if zeroes > count: 
            gamma += '0'
            epsilon += '1'

        else:
            gamma += '1'
            epsilon += '0'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    
    print(gamma*epsilon)
