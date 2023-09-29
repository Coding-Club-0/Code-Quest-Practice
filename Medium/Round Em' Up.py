cases = int(input().rstrip())
data = [''] * cases

for i in range(cases):
    d = list(map(int, input().rstrip().split(" ")))
    for j in range(len(d)): d[j] += (d[j] + 1) % 2 + 1
    data[i] = ' '.join(list(map(str, d)))

for i in range(cases): print(data[i])