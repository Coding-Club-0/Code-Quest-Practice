cases = int(input().rstrip())
from decimal import *
data = [0] * cases
names = [""] * cases
for i in range(cases):
    names[i] = input().rstrip()
    inputs = int(input().rstrip())
    output = []
    for j in range(inputs):
        asterisks, year = input().rstrip().split(" ")
        output.append([int(year), round(Decimal(asterisks) / Decimal(1000))])
    output.sort()
    data[i] = output

for i in range(cases): 
    print(names[i] + ":")
    for j in range(len(data[i])):
        string = ""
        string += f'{data[i][j][0]} {"*" * data[i][j][1]}\n'
        print(string.rstrip())



