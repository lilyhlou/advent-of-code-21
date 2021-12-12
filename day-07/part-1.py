def calculateGas(data, check, gas): #check is point you calculate distance traveled from
    newGas = 0 
    for point in data:
        newGas+= abs(int(point)-int(check))
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
check = sorted(data, key=lambda x: int(x))[int(len(data)/2)]
print(calculateGas(data, check, gas))