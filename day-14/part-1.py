inputs = open("./day14.txt").read().split("\n\n")
pairRulesInput = inputs[1].split("\n")
template = inputs[0]
rules = {}
for rule in pairRulesInput:
    start, insertedLetter = rule.split(' -> ')
    rules[start] = insertedLetter

for _ in range(0, 40):
    pair = [template[0]]
    newString = []
    for c in template[1:]:
        pair.append(c) 
        twoChars = pair[0] + pair[1]
        insertChar = rules[twoChars]
        newString.append(pair.pop(0))
        newString.append(insertChar)
    newString.append(template[-1])
    template = newString
print({i:newString.count(i) for i in newString})



