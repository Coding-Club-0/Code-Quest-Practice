cases = int(input().rstrip())

data = []
for i in range(cases):
    name = input().rstrip().split(".")[1]
    free = True

    for j in range(len(data)):
        if data[j][0] == name:
            data[j][1] += 1
            free = False

    if free: data.append([name, 1])

for d in data:
    print(d[0] + " " + str(d[1]))
