import math
cases = int(input().rstrip())
data = [''] * cases
for i in range(cases):
    N = int(input().rstrip())
    data[i] = [0] * (N+1)
    diff = 0
    for j in range(N):
        v = float(input().rstrip())
        diff += math.ceil(v) - v
        data[i][j] = math.ceil(v)
    data[i][N] = '%.2f' % round(diff, 2)

for i in range(cases):
    for j in range(len(data[i])):
        print(data[i][j])

    