cases = int(input().rstrip())

def encrypt(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    index = 0
    for letter in message:
        if letter not in alphabet: 
            output += letter
            continue
        output += alphabet[(alphabet.index(letter) + alphabet.index(key[index % len(key)])) % len(alphabet)]
        index += 1
    return output

data = [0] * cases
for i in range(cases):
    m = input().rstrip()
    k = input().rstrip()
    data[i] = encrypt(m, k)

for i in range(cases): print(data[i])
