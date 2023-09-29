import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

for d in data:
    for i in range(int(''.ljust(int(d), "1"), 2)+1):
        print(bin(i)[2:].zfill(int(d)))
