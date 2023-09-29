cases = int(input().rstrip())
data = [0] * cases

def convertBool(input):
    return input == "true"

for i in range(cases):
    d = list(map(convertBool, input().rstrip().split(" ")))
    data[i] = not (d[0] ^ d[1])

for i in range(cases):
    print(str(data[i]).lower().strip())