cases = int(input().rstrip())
data = [0] * cases

for i in range(cases):
    d = input().rstrip().split(" ")
    N = int(d[0])
    key = d[1]
    data[i] = [''] * N
    for j in range(N):
        p = input().rstrip().split(" ")
        person = p[0]
        choices = p[1]
        correct = 0
        for k in range(len(key)):
            if key[k] == choices[k]: correct += 1
        score = 100 * correct / len(key)
        letter = "A"
        if score < 60: letter = "F"
        elif score < 70: letter = "D"
        elif score < 80: letter = "C"
        elif score < 90: letter = "B"
        rounded = '%.1f' % round(score, 1)
        data[i][j] = f'{person} {rounded}% {letter}'

for i in range(cases):
    for j in range(len(data[i])):
        print(data[i][j])
