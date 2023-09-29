scores = [2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]
down = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -5, -4, -3, -2, -1, 0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]

cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    d = list(map(int, input().rstrip().split(" ")))
    score = d[0] - d[1]
    c = -16
    data[i] = 1
    for j in range(len(down)):
        if down[j] == score:
            data[i] = scores[j]
            break

for i in range(cases):
    print(data[i])