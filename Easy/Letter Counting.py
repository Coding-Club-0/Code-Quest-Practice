cases = int(input().rstrip())
data = [0] * cases

for i in range(cases): data[i] = len(input().rstrip()) + 1
for i in range(cases): print(data[i])