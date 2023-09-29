cases = int(input().rstrip())
data = [""] * cases
for i in range(cases):
    d = int(input().rstrip())
    if d % 2 == 0: data[i] = "EVEN"
    else: data[i] = "ODD"
for i in range(cases): print(data[i])