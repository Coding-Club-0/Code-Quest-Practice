cases = int(input().rstrip())
data = [""] * cases

for i in range(cases):
    dirs = input().rstrip()
    pos = [0, 0]
    for j in range(len(dirs)):
        if dirs[j] == "L": pos[0] -= 1
        elif dirs[j] == "R": pos[0] += 1
        elif dirs[j] == "U": pos[1] += 1
        elif dirs[j] == "D": pos[1] -= 1
    if pos[0] == 0 and pos[1] == 0: data[i] = "TRUE"
    else: data[i] = "FALSE"

for i in range(cases): print(data[i])