def hasDuplicates(path): #part 2
    for smallCave in ['pn', 'rp', 'ka', 'aw', 'al', 'co', 'az']:
        if path.count(smallCave) >= 2:
            return True
    return False

def findPaths(directions, start, currentPath, count):
    for cave in start:
        duplicate = hasDuplicates(currentPath)
        if cave == 'end':
            count+=1
        elif not (cave in ['pn', 'rp', 'ka', 'aw', 'al', 'co', 'az'] and (cave in currentPath and duplicate)):
            path = currentPath
            path.append(cave)
            count = findPaths(directions, directions[cave], path, count)
    currentPath.pop()
    return count

directions = { 
    'start': ['IV', 'co', 'pn'],
    'pn' : ['TY','co', 'rp', 'aw', 'IV'],
    'TY': ['pn', 'aw', 'co', 'ka'],
    'rp': ['ka', 'end', 'pn', 'al', 'TM'],
    'ka':['rp', 'TY', 'IV'],
    'al': ['IV', 'rp', 'end'],
    'IV': ['al', 'co', 'aw', 'pn', 'ka'],
    'co': ['pn', 'IV', 'TY'],
    'aw': ['TY', 'pn', 'IV', 'PD', 'az'],
    'TM': ['end', 'rp'],
    'PD': ['aw'],
    'az': ['aw']
}
count = 0
print(findPaths(directions, directions['start'], ['start'], count))