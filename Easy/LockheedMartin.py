cases = int(input().rstrip())

text = [""] * cases
for i in range(cases):
    message = int(input().rstrip())
    mult3 = message % 3 == 0
    mult7 = message % 7 == 0
    if mult3 and mult7: text[i] = "LOCKHEEDMARTIN"
    elif mult3: text[i] = "LOCKHEED"
    elif mult7: text[i] = "MARTIN"
    else: text[i] = message

for i in range(cases):
    print(text[i])