cases = int(input().rstrip())
data = [''] * cases
for i in range(cases): data[i] = input().rstrip()
data.sort()
for i in range(cases): print(data[i])