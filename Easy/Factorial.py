def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod

cases = int(input().rstrip())

output = [0] * cases
for i in range(cases):
    output[i] = factorial(int(input().rstrip()))

for i in range(cases):
    print(output[i])

