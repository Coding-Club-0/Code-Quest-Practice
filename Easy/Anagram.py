import sys

cases = int(sys.stdin.readline().rstrip())
data = []
for caseNum in range(cases):
    data.append(sys.stdin.readline().rstrip())

def isAnagram(word1, word2):
    if len(word1) != len(word2): return "NOT AN ANAGRAM"
    elif word1 == word2: return "NOT AN ANAGRAM"
    for letter in word1:
        try:
            i = word2.index(letter)
            word2 = word2[:i] + word2[i+1:]
        except:
            return "NOT AN ANAGRAM"
    return "ANAGRAM"

for d in data:
    d = d.split("|")
    first = d[0]
    second = d[1]
    print(first + "|" + second + " = " + isAnagram(first, second))
