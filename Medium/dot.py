alphabet = "abcdefghijklmnopqrstuvwxyz"

cases = int(input().rstrip())
data = []
for caseNum in range(cases):
    data.append(input().rstrip())

for d in data:
    total = 0
    for letter in d:
        letter = letter.lower()
        if letter in alphabet: total += alphabet.index(letter)+1
    print(total)