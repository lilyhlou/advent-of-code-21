def parsePackage(bits, packageNos):
    version = bits[:3]
    packageNos.append(version)
    bits = bits[3:]
    typeID = bits[:3]
    bits = bits[3:]
    if typeID == '100':
        while not bits[0] == '0':
            bits = bits[5:]
        bits = bits[5:]
        return bits
    else:
        lenTypeID = bits[0]
        bits = bits[1:]
        if lenTypeID == '0':
            subpacketLen = int(bits[:15], 2) 
            bits = bits[15:] 
            subpacket = bits[:subpacketLen]
            while not subpacket == '':
                subpacket = parsePackage(subpacket, packageNos)
            bits = bits[subpacketLen:]
        else: #is 1
            subpacketLen = int(bits[:11], 2)
            bits = bits[11:]
            for i in range(subpacketLen):
                bits = parsePackage(bits, packageNos)
    return bits

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

packageNos = []
for char in data:
    bits+=hexadecimalDict[char]
parsePackage(bits, packageNos)
print(packageNos)
total = 0
for package in packageNos:
    total += int(package, 2)
print(total)