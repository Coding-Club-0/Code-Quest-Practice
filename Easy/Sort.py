cases = int(input().rstrip())

data = [""] * cases
for i in range(cases):
    data[i] = input().rstrip().split(",")
    data[i] = sorted(map(int, data[i]))

for i in range(cases):
    string = ""
    for j in range(len(data[i])):
        string += str(data[i][j]) + ","
    print(string[:-1])

