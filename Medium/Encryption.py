cases = int(input().rstrip())

def substitution(message, alphabet, encrypt):
    alphabet1 = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for letter in message:
        casing = (letter.upper() == letter)
        letter = letter.lower()
        if letter not in alphabet or letter not in alphabet1: 
            string += letter
            continue
        if encrypt: newLetter = alphabet[alphabet1.index(letter)]
        else: newLetter = alphabet1[alphabet.index(letter)]
        if casing: newLetter = newLetter.upper()
        string += newLetter
    return string

data = [""] * cases
for i in range(cases):
    method = input().rstrip()
    encrypt = method == "ENCRYPT"
    key = input().rstrip()

    numMessage = int(input().rstrip())
    data[i] = [""] * numMessage
    for j in range(numMessage):
        message = input().rstrip()
        data[i][j] = substitution(message, key, encrypt)

for i in range(cases):
    for j in range(len(data[i])):
        print(data[i][j].strip())