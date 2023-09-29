cases = int(input().rstrip())
data = [0] * cases

def xorStrings(m, key):
    output = ""
    for i in range(0, len(m), 2):
        b1 = int(m[i:i+2], 16)
        b2 = int(key[i:i+2], 16)
        output += chr(b1 ^ b2)
    return output

for i in range(cases):
    N = int(input().rstrip())
    message = input().rstrip()
    data[i] = [''] * N
    for j in range(N):
        key = input().rstrip()
        data[i][j] = xorStrings(message, key)

for i in range(cases):
    for j in range(len(data[i])):
        print("[" + data[i][j] + "]")
