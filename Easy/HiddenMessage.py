cases = int(input().rstrip())

decoded = [""] * cases
key = input().rstrip()

def toLetter(input):
    return key[int(input)-1]

for i in range(cases-1):
    data = input().rstrip().split(" ")
    for j in range(len(data)):
        data[j] = map(toLetter, data[j].split("-"))
        data[j] = "".join(data[j])
    data = ' '.join(data)
    decoded[i] = data

for i in range(cases-1):
    print(decoded[i].strip())
