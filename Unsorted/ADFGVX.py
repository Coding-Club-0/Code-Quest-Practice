cases = int(input().rstrip())

currentKey = ""
def key1(inp):
    return currentKey.index(inp[0])

for i in range(cases):
    table = []
    for j in range(6):
        table.append(input().rstrip())
        
    key = input().rstrip()
    currentKey = key
    code = input().rstrip()
    grid = []
    leftover = len(code) % len(key)

    spaces = []
    for j in range(leftover):
        spaces.append(str(j))
    for j in range(len(key)-leftover):
        spaces.append("*")

    pair = zip([*key], spaces)
    result = [x for _, x in sorted(pair)]

    for j in range(0, len(code), len(key)):
        grid.append(code[j:j+len(key)])
    
    if leftover != 0:
        output = ""
        currentIndex = 0
        for index in result:
            if index == "*": 
                output += " "
            else: 
                output += grid[-1][currentIndex]
                currentIndex += 1
        grid[-1] = output
    
    for j in range(len(grid)):
        pair = zip(sorted([*key]), [*grid[j]])
        result = [x for _, x in sorted(pair, key=key1)]
        grid[j] = ''.join(result)
    
    realCode = ''.join(grid).rstrip()
    string = "ADFGVX"

    decrypted = ""
    for j in range(0, len(realCode), 2):
        i1 = string.index(realCode[j])
        j1 = string.index(realCode[j+1])
        decrypted += table[i1][j1]
    print(decrypted)