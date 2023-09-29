cases = int(input().rstrip())
data = [""] * cases

for i in range(cases):
    d = input().rstrip().split(" ")
    output = ""
    for j in range(len(d)):
        if d[j] == "M": output += str(j + 1) + " "
    data[i] = output.rstrip()

for i in range(cases): print(data[i])
    