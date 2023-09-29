cases = int(input().rstrip())
data = [""] * cases

def getBin(num): return bin(num)[2:].zfill(8)

def bitsInCommon(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]: return i
    return len(str1) - 1

def andStrings(str1, str2):
    output = ""
    for i in range(len(str1)):
        if str1[i] == "1" and str2[i] == "1": output += "1"
        else: output += "0"
    ipAddress = ""
    for i in range(0, len(output), 8):
        integer = int(output[i:i+8], 2)
        ipAddress += str(integer) + "."
    return ipAddress[:-1]

def allTheSame(arr):
    first = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != first: return False
    return True

for i in range(cases):
    num = int(input().rstrip())
    addresses = [""] * num
    for j in range(num): addresses[j] = ''.join(list(map(getBin, map(int, input().rstrip().split(".")))))

    if allTheSame(addresses):
        lastBit = 0
        for j in range(len(addresses[0])-1, 0, -1):
            if addresses[0][j] != "0": 
                lastBit = j-1
                break
        data[i] = f'{andStrings("".ljust(lastBit, "1"), addresses[0])}/{lastBit}'
        continue

    leastInCommon = 32
    for j in range(num):
        for k in range(num):
            if j != k:
                inCommon = bitsInCommon(addresses[j], addresses[k])
                if inCommon < leastInCommon:
                    leastInCommon = inCommon
    data[i] = andStrings(("".ljust(leastInCommon, "1") + "".ljust(32-leastInCommon, "0")), addresses[0]) + "/" + str(leastInCommon)

for i in range(cases): print(data[i].strip())
    


