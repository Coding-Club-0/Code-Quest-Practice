cases = int(input().rstrip())
data = [""] * cases
for i in range(cases):
    num = int(input().rstrip())

    for j in range(num):
        d = input().rstrip()
        d = d.split("|")
        word = d[0]
        index = int(d[1])
        data[i] += word[index]
    
for i in range(cases):
    print(data[i])
