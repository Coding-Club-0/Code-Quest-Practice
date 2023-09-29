def shift(letter, amt, dir):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    a = -amt * (2 * dir-1)
    i = (alphabet.index(letter)+a) % 26
    if (amt < 0): i += 26
    return alphabet[i]

def decrypt(message, amts, dirs):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    specialChars = 0
    for i in range(len(message)):
        letter = message[i].lower()
        if letter not in alphabet:
            string += letter
            specialChars += 1
            continue

        string += shift(letter, amts[(i - specialChars) % len(amts)], dirs[(i - specialChars) % len(dirs)])
    return string

cases = int(input().rstrip())

def toInt(arr):
    newArr = []
    for str in arr:
        newArr.append(int(str))
    return newArr

messages = [""] * cases
amts = [""] * cases
dirs = [""] * cases
for i in range(cases):
    messages[i] = input().rstrip()
    amts[i] = toInt(input().rstrip().split(" "))
    dirs[i] = toInt(input().rstrip().split(" "))

for i in range(cases):
    print(decrypt(messages[i], amts[i], dirs[i]))