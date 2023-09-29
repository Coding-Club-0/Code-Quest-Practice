strings = "Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu"
strings = strings.split(" ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
cases = int(input().rstrip())

encoded = [""] * cases
for i in range(cases):
    words = int(input().rstrip())
    encoded[i] = [""] * words
    for j in range(words):
        sentence = input().rstrip()
        string = ""
        for k in range(len(sentence)):
            try:
                string += (strings[alphabet.index(sentence[k][0].lower())]) + "-"
            except:
                string += " "
        string = string.replace("- ", " ")[:-1]
        encoded[i][j] = string

for i in range(cases):
    for j in range(len(encoded[i])):
        print(encoded[i][j])  
        