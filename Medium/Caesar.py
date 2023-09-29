def caesar(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string  = ""
    for letter in message:
        letter = letter.lower()
        if letter not in alphabet: string += letter
        else:
            mult = int(shift/26)
            num = alphabet.index(letter) - shift
            if num < 0: num += 26*mult
            string += alphabet[(num) % 26]
    return string

cases = int(input().rstrip())

decrypted = [""] * cases
for i in range(cases):
    shift = int(input().rstrip())
    message = input().rstrip()
    decrypted[i] = caesar(message, shift)

for i in range(cases):
    print(decrypted[i])
