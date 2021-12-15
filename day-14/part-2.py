inputs = open("./day14.txt").read().split("\n\n")
pairRulesInput = inputs[1].split("\n")

template = inputs[0] #line read from text file

rules = {}
for rule in pairRulesInput:
    start, insertedLetter = rule.split(' -> ')
    rules[start] = insertedLetter

atoms = list(set(''.join(rules.keys())+ ''.join(rules.values())))
elementCounts = {}.fromkeys(atoms, 0)
pairs = rules.fromkeys(rules.keys(), 0)

#populate initial dictionary
start = [template[0]]
elementCounts[template[0]] = 1
for c in template[1:]:
    start.append(c) 
    elementCounts[c] = elementCounts[c] + 1
    twoChars = start[0] + start[1]
    pairs[twoChars] = pairs[twoChars] + 1
    start.pop(0)

# iterate through dictionary and add letters    
for _ in range(0, 40):
    newPairs = rules.fromkeys(rules.keys(), 0)
    for pair in pairs:
        if pairs[pair] > 0:
            newPairs[pair[0] + rules[pair]] = newPairs[pair[0] + rules[pair]] +  pairs[pair]
            newPairs[rules[pair]+pair[1]] = newPairs[rules[pair]+pair[1]] +  pairs[pair]
            elementCounts[rules[pair]] = elementCounts[rules[pair]] + pairs[pair]
    pairs = newPairs
print(max(elementCounts.values())-min(elementCounts.values()))

