import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())
    
for case in data:
    case = case.split(" ")
    a = int(case[0])
    b = int(case[1])

    print(str(a+b) + " " + str(a*b))


