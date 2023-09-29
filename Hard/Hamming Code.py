cases = int(input().rstrip())
data = [""] * cases
for i in range(cases):
    num = int(input().rstrip())
    d = [""] * num
    for l in range(num):
        binary = input().rstrip()
        bits = len(bin(len(binary)))-2
        counts = [0] * bits
        
        count = 0
        for j in range(1, 2**bits):
            try:
                current = bin(j)[2:].zfill(bits)
                if current.count("1") == 1: continue
                for k in range(bits):
                    if current[k] == "1" and binary[count] == "1": counts[k] += 1
                count += 1
            except: break

        result = ""
        count = 0
        for j in range(1, 2**bits):
            try:
                current = bin(j)[2:].zfill(bits)
                if current.count("1") == 1: 
                    index = current.index("1")
                    result += str((counts[index]) % 2)
                else:
                    result += binary[count]
                    count += 1
            except: break
        d[l] = result
    data[i] = '\n'.join(d).rstrip()

for i in range(cases): print(data[i])