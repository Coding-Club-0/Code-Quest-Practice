import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

for d in data:
    d = d.split(" ")
    r = float(d[0])
    w = int(float(d[1]))
    h = int(float(d[2]))

    results = []
    for x in range(w+1):
        for y in range(h+1):
            if x**2 + y**2 > r**2: results.append(str(x) + "," + str(y))
    
    for num in results:
        print(num)