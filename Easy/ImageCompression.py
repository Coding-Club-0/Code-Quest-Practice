cases = int(input().rstrip())

data = [0] * cases
for i in range(cases):
    num = int(input().rstrip())
    data[i] = [0] * num
    for j in range(num):
        data[i][j] = float(input().rstrip())

for i in range(cases):
    maxValue = -20000000
    minValue = 20000000
    for j in range(len(data[i])):
        if data[i][j] > maxValue: maxValue = data[i][j]
        if data[i][j] < minValue: minValue = data[i][j]
    
    for j in range(len(data[i])):
        print(round(255 * (data[i][j] - minValue) / (maxValue - minValue) ))
