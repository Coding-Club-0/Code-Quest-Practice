cases = int(input().rstrip())

data = [0] * cases
for i in range(cases):
    N = int(input().rstrip())
    data[i] = [0] * N
    for j in range(N):
        p = int(input().rstrip())

        data[i][j] = "Yes"
        if p < 1582: data[i][j] = "No"
        elif p % 4 != 0: data[i][j] = "No"
        elif p % 100 == 0: data[i][j] = "No"
        if p % 400 == 0: data[i][j] = "Yes"
    
for i in range(cases):
    for j in range(len(data[i])):
        print(data[i][j])