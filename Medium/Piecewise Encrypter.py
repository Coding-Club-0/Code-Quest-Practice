cases = int(input().rstrip())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
data = [""] * cases
def gcf(num):
    for i in range(num-1, 1, -1):
        if num % i == 0: return i
    return 1

for i in range(cases):
    word = [*input().rstrip()]
    output = ""
    for j in range(len(word)):
        if word[j].upper() in alphabet:
            numerical = alphabet.index(word[j].upper()) + 1
            # print(numerical)
            if numerical <= 5: numerical += 6
            elif numerical <= 10: numerical **= 2
            elif numerical <= 15: numerical = (numerical % 3) * 5 + 1
            elif numerical <= 20: 
                firstDigit = numerical % 10
                numerical //= 10
                secondDigit = numerical
                numerical = 8 * (firstDigit + secondDigit)
            else: numerical = 2 * gcf(numerical)
            output += alphabet[(numerical-1) % 26]
            # print(numerical)
        else: output += word[j]
    data[i] = output

for i in range(cases): print(data[i])
