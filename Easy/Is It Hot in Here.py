cases = int(input().rstrip())

data = [''] * cases
for i in range(cases):
    N = int(input().rstrip())
    data[i] = [''] * N
    for j in range(N):
        p = input().rstrip()
        q = p.split(" ")
        temp = float(q[0])
        isFar = q[1] == "F"
        if isFar: data[i][j] = p + " = " + '%.1f' % round(5/9 * (temp - 32), 1) + " C"
        else: data[i][j] = p + " = " + '%.1f' % round(9/5 * temp + 32, 1) + " F"

for i in range(cases):
    for j in range(len(data[i])):
        print(data[i][j])

