with open("./day8.txt") as file:
    data = [line.strip() for line in file]
    count = 0
    sumAll = 0 #sum of the total numbers
    translateLetters = {} #maps number to chars it corresponds to
    for line in data: 
        lines = line.split(" | ")
        alphabet = sorted(lines[0].split(), key=len)
        translateLetters = { ''.join(sorted(alphabet[9])) : 8}
        # compare numbers to 4 and 1 to get result
        fourStr = ''
        oneStr = ''
        for number in alphabet[:9]:
            length = len(number)
            if length < 5:
                if length == 2: 
                    translateLetters[''.join(sorted(number))] = 1
                    oneStr = sorted(number)
                elif length == 3:
                    translateLetters[''.join(sorted(number))] = 7
                else: 
                    translateLetters[''.join(sorted(number))] = 4
                    fourStr = sorted(number)
            elif length == 5:
                counter = 0
                for letter in fourStr: #shares 3 values w 4 its either 5 or 2
                    if letter in number:
                        counter+=1
                if counter == 3: #either 3 or 5
                    counter = 0 
                    for letter in oneStr: 
                        if letter in number:
                            counter+=1 
                    if counter == 2: 
                        translateLetters[''.join(sorted(number))] = 3
                    else: 
                        translateLetters[''.join(sorted(number))] = 5
                else:
                    translateLetters[''.join(sorted(number))] = 2
            else:
                counter = 0
                for letter in oneStr: 
                    if letter in number:
                        counter+=1
                if counter == 2:
                    counter = 0
                    for letter in fourStr:
                        if letter in number:
                            counter+=1
                    if counter == 4:
                        translateLetters[''.join(sorted(number))] = 9
                    else:
                        translateLetters[''.join(sorted(number))] = 0
                else:
                    translateLetters[''.join(sorted(number))] = 6
        messages = lines[1].split()
        totalNumbers = 0
        for number in messages:
            numberString = ''.join(sorted(number))
            if numberString in translateLetters:
                totalNumbers = totalNumbers * 10 + int(translateLetters[numberString])
        sumAll += totalNumbers
        print(sumAll)