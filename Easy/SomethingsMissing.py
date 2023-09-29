cases = int(input().rstrip())

data = [""] * cases
for i in range(cases):
    m = input().rstrip().split(" ")
    word = [*m[0]]
    word.pop(int(m[1]))
    data[i] = ''.join(word)

for i in range(cases):
    print(data[i])