cases = int(input().rstrip())
data = [0] * cases
for i in range(cases): data[i] = input().rstrip()
VOWELS = "aeiou"
for i in range(cases):
    decoded = ""
    j = 0
    while j < len(data[i]):
        if data[i][j].lower() in VOWELS: 
            decoded += data[i][j+1]
            j += 1
        j += 1
    print(decoded) 