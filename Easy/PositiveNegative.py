cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    p = int(input().rstrip()) > 0
    if p: data[i] = "POSITIVE"
    else: data[i] = "NEGATIVE"
for i in range(cases): print(data[i])