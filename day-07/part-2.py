def calculateGas(data, check, gas): #check is point you calculate distance traveled from
    newGas = 0 
    for point in data:
        difference = int(abs(int(point)-int(check)))
        newGas+= (difference*(difference+1))/2
    if newGas < gas or gas == 0:
        gas = newGas
        less = calculateGas(data, int(check)-1, int(gas))
        if less < newGas: 
            return calculateGas(data, int(check)-1, int(gas))
        more = calculateGas(data, int(check)+1, int(gas))
        if more < newGas:
            return calculateGas(data, int(check)+1, int(gas))
    return gas


data = open("./day7.txt").read().split(",")
gas = 0
check = sum(int(i) for i in data)/len(data) 
print(calculateGas(data, check, gas))