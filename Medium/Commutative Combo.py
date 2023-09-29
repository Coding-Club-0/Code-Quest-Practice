cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    findSum = int(input().rstrip().split("=")[1])
    values = list(map(int, input().rstrip()))
    