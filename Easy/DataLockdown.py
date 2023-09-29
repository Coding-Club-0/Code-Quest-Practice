cases = int(input().rstrip())

result = [''] * cases
for i in range(cases):
    result[i] = []
    num = int(input().rstrip())
    for j in range(num):
        data = input().rstrip().split(" ")
        site = data[0]
        size = int(data[1])
        if '.lmco.com' in site: continue
        if size > 1000: result[i].append(f"{site} {size}")

for i in range(cases):
    for j in range(len(result[i])):
        print(result[i][j])