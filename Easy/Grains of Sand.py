cases = int(input().rstrip())

data = [0] * cases
for i in range(cases):
    N = int(input().rstrip())
    sum = 0
    for j in range(N):
        sum += int(input().rstrip())
    data[i] = sum

for i in range(cases):
    print(data[i])