cases = int(input().rstrip())
data = [""] * cases

for i in range(cases):
    first, second, result = list(map(int, input().rstrip().split(" ")))
    if first + second == result: data[i] = "Addition"
    elif first - second == result: data[i] = "Subtraction"
    elif first * second == result: data[i] = "Multiplication"
    elif int(first / second) == result: data[i] = "Division"
    elif first % second == result: data[i] = "Modulo"

for i in range(cases): print(data[i])
