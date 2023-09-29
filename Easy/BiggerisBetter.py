import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

for d in data:
    d = d.split(" ")
    maxValue = -1
    for i in range(len(d)):
        if int(d[i]) > maxValue:
            maxValue = int(d[i])
    print(maxValue)