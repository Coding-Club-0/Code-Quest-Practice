import sys
import math

cases = int(input().rstrip())
data = [0] * cases
data2 = [0] * cases
for i in range(cases):
    num = int(input().rstrip())
    data[i] = [0] * num
    data2[i] = [0] * num

    for j in range(num):
        data[i][j] = input().rstrip()


for i in range(len(data)):
    for j in range(len(data[i])):
        d = data[i][j].split(" ")
        a = int(d[0])
        b = int(d[1])
        data2[i][j] = math.sqrt(a**2 + b**2)

for i in range(len(data)):
    newArr = [x for _, x in sorted(zip(data2[i], data[i]))]
    for j in range(len(newArr)):
        print(newArr[j])