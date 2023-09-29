import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

alphabet = "abcdefghijklmnopqrstuvwxyz"
def hasLetters(word1, word2):
    for letter in word2:
        if letter not in alphabet: continue
        elif letter not in word1: 
            return False
    return True

for d in data:
    d = d.split("|")
    first = d[0].lower()
    second = d[1].lower()
    isSpy = hasLetters(first, second)

    if isSpy: print("That's my secret contact!")
    else: print("You're not a secret agent!")