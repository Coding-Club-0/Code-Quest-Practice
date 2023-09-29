import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

for d in data:
    d = d.split(" ")
    string = ""
    for i in range(len(d)):
        num = float(d[i])
        string += ('%.2f' % round(((num + 180) % 360), 2)).zfill(6) + " "
    print(string.rstrip())