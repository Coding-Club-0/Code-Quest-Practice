cases = int(input().rstrip())

data = [""] * cases
for i in range(cases):
    line = list(map(int, input().rstrip().split(" ")))
    if line[0] > line[1]: data[i] = "Times has " + str(line[0] - line[1]) + " more subscribers"
    elif line[1] > line[0]: data[i] = "Herald has " + str(line[1] - line[0]) + " more subscribers"
    elif line[1] == line[0]: data[i] = "Times and Herald have the same number of subscribers"

for i in range(cases):
    print(data[i].strip())