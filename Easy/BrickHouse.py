cases = int(input().rstrip())

data = [''] * cases
for i in range(cases):
    d = list(map(int, input().rstrip().split(' ')))

    canBuild = False
    for j in range(0, d[0]+1):
        sum = 0
        for k in range(0, d[1]+1):
            sum = j + k * 5
            if sum == d[2]: 
                canBuild = True
                break
    data[i] = ["false", "true"][int(canBuild)]

for i in range(cases):
    print(data[i])