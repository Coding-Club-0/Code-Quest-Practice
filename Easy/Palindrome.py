def palindrome(string):
    return string.lower() == string.lower()[::-1]

cases = int(input().rstrip())
data = [''] * cases

def printArr(arr):
    string = ""
    for elem in arr:
        string += str(elem) + ", "
    return string[:-2]

for i in range(cases):
    isntPalindrome = []
    num = int(input().rstrip())
    for j in range(num):
        inp = input().rstrip()
        if not palindrome(inp):
            isntPalindrome.append(j+1)
    if len(isntPalindrome) == 0: data[i] = "True"
    else: data[i] = "False - " + printArr(isntPalindrome)

for i in range(cases):
    print(data[i])