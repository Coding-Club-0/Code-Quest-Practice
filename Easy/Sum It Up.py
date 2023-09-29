cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    first, second = list(map(int, input().rstrip().split(" ")))
    if first != second: data[i] = first + second
    else: data[i] = 2 * (first + second)

for i in range(cases): print(data[i])