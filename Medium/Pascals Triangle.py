def factorial(n):
    prod = 1
    for i in range(2, n+1): prod *= i
    return prod

def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

cases = int(input().rstrip())
data = [0] * cases
for i in range(cases):
    v = int(input().rstrip())
    data[i] = int(choose(v, v//2))

for i in range(cases): print(data[i])