import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

nums = [2, 4, 4]
for d in data:
    d = d.split(" ")
    count = 0
    for i in range(3):
        count += nums[i] * int(d[i])
    print(count)
