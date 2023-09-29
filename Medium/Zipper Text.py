cases = int(input().rstrip())
data = [""] * cases

filterU = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ-")
filterL = set("abcdefghijklmnopqrstuvwxyz=")

for i in range(cases):
    U = int(input().rstrip())
    lengthsU = list(map(int, input().rstrip().split(" ")))
    L = int(input().rstrip())
    lengthsL = list(map(int, input().rstrip().split(" ")))

    encoded = ""
    while True:
        string = input().rstrip()
        encoded += string
        if len(string) < 80: break
    
    decodedU = ''.join(filter(filterU.__contains__, encoded)).replace("-", " ")
    decodedL = ''.join(filter(filterL.__contains__, encoded)).replace("=", " ")

    index = 0
    for j in range(len(lengthsU)):
        index += lengthsU[j]
        decodedU = decodedU[:index+j] + "\n" + decodedU[index+j:]

    index = 0
    for j in range(len(lengthsL)):
        index += lengthsL[j]
        decodedL = decodedL[:index+j] + "\n" + decodedL[index+j:]
    
    print(decodedU)
    print(decodedL.rstrip())