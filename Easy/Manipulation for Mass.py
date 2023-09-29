cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    d = list(map(float, input().rstrip().split(" ")))
    data[i] = d[0] * d[1]
for i in range(cases): print('%.2f' % round(data[i], 2))