cases = int(input().rstrip())
output = [0] * cases

for i in range(cases):
    d = input().rstrip().split(" ")
    num = d[0]
    order = d[1]
    
    if order == "LITTLE":
        newNum = ""
        for j in range(0, len(num), 2):
            newNum = num[j:j+2] + newNum
        num = newNum
    
    output[i] = int(num, 16)

for i in range(cases):
    print(output[i])

    

