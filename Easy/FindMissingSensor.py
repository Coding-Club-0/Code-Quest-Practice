cases = int(input().rstrip())

results = [''] * cases
for i in range(cases):
    N = int(input().rstrip())

    arr = sorted(map(int, input().rstrip().split(" ")))
    for j in range(len(arr)):
        if arr[j] != (j + 1):
            results[i] = (j + 1)
            break
    if results[i] == '': results[i] =  results[i] = N

for i in range(cases):
    print(results[i])