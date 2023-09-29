cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    p = list(map(int, input().rstrip().split(" ")))
    inp = input().strip().split(" ")

    w = p[0]
    h = p[1]

    new_str = [[]]
    size = 0
    for j in range(len(inp)):
        if len(inp[j]) > w:
            data[i] = "WILL NOT FIT"
            break
        if size + len(inp[j])  > w:
            new_str.append([])
            size = 0
        new_str[-1].append(inp[j])
        size += len(inp[j]) + 1
        
    if data[i] == "WILL NOT FIT": continue
    if len(new_str) > h:
        data[i] = "WILL NOT FIT"
    else:
        string = ""
        for j in range(len(new_str)):
            current = ""
            for k in range(len(new_str[j])):
                current += new_str[j][k] + " "
            string += current.strip() + "\n"
        data[i] = string.strip()

for i in range(cases):
    print(data[i])