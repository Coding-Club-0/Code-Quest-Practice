cases = int(input().rstrip())

def shareLetters(a, b):
    if len(a) != len(b): return False
    for i in range(len(a)):
        if a[i] in b:
            index = b.index(a[i])
            b = [*b]
            b.pop(index)
            b = ''.join(b)
        else:
            return False
    return True

def haveFirstAndLast(a, b):
    return a[0] == b[0] and a[-1] == b[-1]

data = [''] * cases
for i in range(cases):
    misspelled, correct = input().rstrip().split(" ")
    data[i] = correct if (shareLetters(misspelled, correct) and haveFirstAndLast(misspelled, correct)) else misspelled
for i in range(cases): print(data[i])