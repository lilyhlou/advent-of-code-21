def explodeNumber(current): 
    bracketCount = 0 
    i = 0
    while i < len(current):
        if bracketCount == 5:
            leftNumberIndex = i-1
            rightNumberIndex = i
            while current[rightNumberIndex] != ']':
                rightNumberIndex+=1
            #get bracket to be exploded
            explodeNumber = current[leftNumberIndex+1:rightNumberIndex].split(",") #number without brackets
            left = explodeNumber[0]
            right = explodeNumber[1]
            current = current[:leftNumberIndex] + "0" + current[rightNumberIndex+1:] 
            rightNumberIndex = leftNumberIndex + 1 #skip zero added
            leftNumberIndex -= 1 #for adding zero
            while leftNumberIndex > 0 and current[leftNumberIndex] == '[' or current[leftNumberIndex] == ']' or current[leftNumberIndex] == ',':
                leftNumberIndex-=1
            if leftNumberIndex > 0:
                currentLeftNum = current[leftNumberIndex]
                x=1
                while leftNumberIndex-x > 0 and current[leftNumberIndex-x:leftNumberIndex+1].isnumeric():
                    currentLeftNum = current[leftNumberIndex-x:leftNumberIndex+1]
                    x+=1
                leftSum = int(currentLeftNum) + int(left)
                if len(str(leftSum)) == 2:
                    rightNumberIndex+=1
                current= current[:leftNumberIndex-len(str(currentLeftNum))+1] + str(leftSum) + current[leftNumberIndex+1:]
            while rightNumberIndex < len(current) and (current[rightNumberIndex] == ']' or current[rightNumberIndex] == ',' or current[rightNumberIndex] == '['):
                rightNumberIndex+=1
            if rightNumberIndex < len(current):
                currentRightNum = current[rightNumberIndex]
                x=1
                while rightNumberIndex+x < len(current) and current[rightNumberIndex:rightNumberIndex+x+1].isnumeric():
                    currentRightNum = current[rightNumberIndex:rightNumberIndex+x+1]
                    x+=1
                rightSum = int(currentRightNum) + int(right)
                current= current[:rightNumberIndex] + str(rightSum) + current[rightNumberIndex+len(str(currentRightNum)):]
            bracketCount = 0 
            i = 0 
            continue
        if current[i] == '[':
            bracketCount+=1
        if current[i] == ']':
            bracketCount-=1
        i+=1
    return current
    
def split(current):
    i=1
    while i < len(current): 
        if current[i-1:i+1].isnumeric():
            splitNumber = current[i-1:i+1]
            div, mod = divmod(int(splitNumber), 2)
            current = current[:i-1] + '['+str(div)+","+str(div+mod)+"]"+current[i+1:]
            bracketCount = 0 
            i = 1
            current = explodeNumber(current)
        else:
            i+=1
    return current

def parseCurrent(current):
    current = explodeNumber(current)
    current = split(current)
    return current
def calculateMagnitude(current):
    #find every comma
    i = 0
    while i < len(current):
        if current[i] == ',':
            leftNumLen = 1
            rightNumLen = 1
            if current[i-leftNumLen].isnumeric() and current[i+rightNumLen].isnumeric():
                while current[i-leftNumLen:i].isnumeric():
                    leftNumLen+=1
                while current[i+1:i+rightNumLen+1].isnumeric():
                    rightNumLen+=1
                leftNumLen-=1
                rightNumLen-=1
                left = current[i-leftNumLen:i]
                right = current[i+1:i+rightNumLen+1]
                result = int(left)*3+int(right)*2
                current=current[:i-leftNumLen-1]+str(result)+current[i+rightNumLen+2:]
                i=0
                continue
        i+=1   
    return current
    
with open("./day18.txt") as file:
    data = [line.strip() for line in file]
    current = data[0]
    for line in data[1:]:
        current = "["+current+","+line+"]"
        current = parseCurrent(current)
    print(calculateMagnitude(current))