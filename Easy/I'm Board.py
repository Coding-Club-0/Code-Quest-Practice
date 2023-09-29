cases = int(input().rstrip())

data = [''] * cases

for i in range(cases):
    N = int(input().rstrip())
    string = ""
    for j in range(N):
        substring = ""
        for k in range(N):
            substring += "# "
        string += substring.strip() + "\n"
    data[i] = string.strip()

for i in range(cases):
    print(data[i])