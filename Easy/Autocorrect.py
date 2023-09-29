import sys

cases = int(sys.stdin.readline().rstrip())
dictionaries = [0] * cases
words = [0] * cases

for i in range(cases):
    data = input("").rstrip().split(" ")
    entries = data[0]
    numWords = data[1]

    dictionaries[i] = [0] * entries
    words[i] = [0] * numWords

    for j in range(entries):
        dictionaries[i][j] = input("").rstrip()

    for j in range(numWords):
        words[i][j] = input("").rstrip()

def hamming(word1, word2):
    if len(word1) != len(word2): return -2
    count = 0
    for i in range(len(word1)):
        if word1[i].lower() == word2[i].lower(): count += 1

    return count

for i in range(cases):
    dictionary = dictionaries[i]
    words = words[i]

    for j in range(len(words)):
        maxValue = -1
        maxWord = ""
        for k in range(len(dictionary)):
            h = hamming(words[j], dictionary[k])
            if h > maxValue:
                maxValue = h
                maxWord = dictionary[k]
        print(maxWord)



