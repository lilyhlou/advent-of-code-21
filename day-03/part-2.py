with open("./day3.txt") as file:
    data = [line.strip() for line in file]
    o2 = data
    co2 = data
    ones = []
    zeroes = []
    i = 0
    while i < 12 and len(o2) > 1:
        for number in o2: 
            if number[i] == '1':
                ones.append(number)
            else:
                zeroes.append(number)
        if len(zeroes) > len(ones): 
            o2 = zeroes
        else: 
            o2 = ones
        zeroes = []
        ones = []
        i+=1
    i = 0
    while i < 12 and len(co2) > 1:
        for number in co2: 
            if number[i] == '1':
                ones.append(number)
            else:
                zeroes.append(number)
        if len(zeroes) <= len(ones): 
            co2 = zeroes
        else: 
            co2 = ones
        zeroes = []
        ones = []
        i+=1
    print(int(o2[0],2)*int(co2[0],2))
