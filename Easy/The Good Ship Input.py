cases = int(input().rstrip())
data = [""] * cases

def inArray(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

for i in range(cases):
    X, Y = list(map(int, input().rstrip().split(" ")))

    database = [""] * X
    for j in range(X): database[j] = input().rstrip()
    computer = [""] * Y
    for j in range(Y): computer[j] = input().rstrip()

    output = []
    for j in range(X):
        if computer.count(database[j]) == 0: output.append(database[j])
    output.sort()
    data[i] = output
for i in range(cases): 
    for o in data[i]:
        print(o.rstrip())
        
    
