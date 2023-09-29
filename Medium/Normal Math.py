cases = int(input().rstrip())
data = [""] * cases
import math

for i in range(cases):
    w, h = list(map(int, input().rstrip().split(" ")))
    value = 0
    for j in range(w):
        a = list(map(int, input().rstrip().split(" ")))
        for num in a:
            value += num ** 2
    data[i] = '%.2f' % round(math.sqrt(value), 2)

for i in range(cases): print(data[i])

