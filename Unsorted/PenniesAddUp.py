cases = int(input().rstrip())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def valueOfWord(word, startingValue):
    s = 0
    for letter in word:
        value = (alphabet.index(letter) + startingValue) % 26
        s += value
    return s


for case in range(cases):
    valueOfA, words = map(float, input().rstrip().split(" "))
    
    for word in range(int(words)):
        w = input().rstrip()
        value = valueOfWord(w, valueOfA)
        if value == 100:
            print(f'WINNER {int(valueOfA)}: {w}')
