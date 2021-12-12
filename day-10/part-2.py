with open("./day10.txt") as file:
    data = [line.strip() for line in file]
    matchingDelimiters = {
        ')': '(',
        '}' : '{',
        ']': '[',
        '>':'<',
        '(': ')',
        '{' : '}',
        '[' : ']',
        '<' : '>'
    }
    delimiterPoints = {
    ')': 1,
    '}': 3,
    ']': 2,
    '>': 4 
    }
    score = []
    i = 0 
    # get rid of corrupted lines
    while i < len(data):
        stack = []
        for delimiter in data[i]:
            if delimiter in ['(', '[', '{', '<']:
                stack.append(delimiter)
            else:
                if not matchingDelimiters[delimiter] == stack.pop():
                    data.pop(i)
                    i-=1
                    break
        i+=1
    for incomplete in data:
        points = 0 
        stack = []
        for delimiter in incomplete:
            if delimiter in ['(', '[', '{', '<']:
                stack.append(delimiter)
            else:
                stack.pop()
        for remainingDelimiters in reversed(stack): 
            points=points*5 + delimiterPoints[matchingDelimiters[remainingDelimiters]]
        score.append(points)
    print(sorted(score)[int(len(score)/2)])
