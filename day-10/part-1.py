with open("./day10.txt") as file:
    data = [line.strip() for line in file]
    matchingDelimiters = {
        ')': '(',
        '}' : '{',
        ']': '[',
        '>':'<'
    }
    delimiterPoints = {
    ')': 3,
    '}' : 1197,
    ']': 57,
    '>':25137 
    }

    corruptedChars = []

    for chunk in data:
        stack = []
        for delimiter in chunk:
            if delimiter in ['(', '[', '{', '<']:
                stack.append(delimiter)
            else:
                if not matchingDelimiters[delimiter] == stack.pop():
                    corruptedChars.append(delimiter)
                    break
    points = 0
    print(corruptedChars)
    for char in corruptedChars:
        points+= int(delimiterPoints[char])
    print(points)