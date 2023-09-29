cases = int(input().rstrip())
data = [0] * cases

def getFirst(input):
    return input[0].upper()

for i in range(cases):
    N = int(input().rstrip())
    data[i] = [0] * N
    for j in range(N): data[i][j] = list(map(getFirst, input().rstrip().split(" ")))

for i in range(cases):
    for j in range(len(data[i])):
        print(data[i][j][0] + data[i][j][2] + data[i][j][1])