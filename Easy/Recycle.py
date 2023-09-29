cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    aluminum, plastic, glass = list(map(int, input().rstrip().split(" ")))
    numAluminum = aluminum * 31
    numPlastic = plastic * 15
    numGlass = glass // 2
    data[i] = f'${"%.2f" % round(0.05 * numAluminum + 0.1 * numPlastic + 0.2 * numGlass, 2)}'

for i in range(cases): print(data[i])