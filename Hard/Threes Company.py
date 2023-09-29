cases = int(input().rstrip())
data = [""] * cases
for i in range(cases):
    triplets, inputs = list(map(int, input().rstrip().split(" ")))
    operations = []
    for j in range(triplets):
        a = input().rstrip().split(" ")
        for test in a:
            if "!" in test: operations.append("!")
            else: operations.append("")
    
    for j in range(inputs):
        inp = input().rstrip().replace(" ", "")
        count = 0
        for k in range(0, len(inp), 3):
            a = list(map(bool, list(map(int, [*inp[k:k+3]]))))
            for l in range(k, k+3):
                if operations[l] == "!":
                    a[l-k] = not a[l-k]
            count += int(a[0] or a[1] or a[2])

        if (count < triplets): data[i] += "FALSE\n"
        else: data[i] += "TRUE\n"
for i in range(cases): print(data[i].rstrip())
        
