cases = int(input().rstrip())
data = [''] * cases

def convertToBinary(string):
    return string.replace("A", "0").replace("T", "0").replace("G", "1").replace("C", "1")

for i in range(cases):
    d = input().rstrip()
    string = ""
    d = convertToBinary(d)
    for j in range(0, len(d), 7):
        string += chr(int(d[j:j+7], 2))
    data[i] = string

for i in range(cases): print(data[i])
