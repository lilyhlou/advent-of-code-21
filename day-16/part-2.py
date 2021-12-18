def parsePackage(bits):
    version = bits[:3]
    bits = bits[3:]
    typeID = bits[:3]
    bits = bits[3:]
    result = 0
    numbers = []
    if typeID == '100':
        packetval = ''
        while not bits[0] == '0':
            packetval+=bits[1:5]
            bits = bits[5:]
        packetval+=bits[1:5]
        packetval = int(packetval, 2)
        bits = bits[5:]
        return packetval, bits
    else:
        lenTypeID = bits[0]
        bits = bits[1:]
        if lenTypeID == '0':
            subpacketLen = int(bits[:15], 2) 
            bits = bits[15:] 
            subpacket = bits[:subpacketLen]
            while not subpacket == '':
                value, subpacket = parsePackage(subpacket)
                numbers.append(value)
            bits = bits[subpacketLen:]
        else: #is 1
            subpacketLen = int(bits[:11], 2)
            bits = bits[11:]
            for i in range(subpacketLen):
                value, bits = parsePackage(bits)
                numbers.append(value)
        if typeID == '000':
            result = sum(numbers)
        elif typeID == '001':
            result = 1
            for n in numbers:
                result = result * n
        elif typeID == '010':
            result = min(numbers)
        elif typeID == '011':
            result = max(numbers)
        elif typeID == '101':
            if numbers[0] > numbers[1]:
                result = 1
            else:
                result = 0
        elif typeID == '110':
            if numbers[0] < numbers[1]:
                result = 1
            else:
                result = 0
        elif typeID == '111':
            if numbers[0] == numbers[1]:
                result = 1
            else:
                result = 0
    return result, bits

data = open("./day16.txt").read()
bits = ''
hexadecimalDict = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
}
for char in data:
    bits+=hexadecimalDict[char]

print(parsePackage(bits))
