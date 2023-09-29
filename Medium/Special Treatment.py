cases = int(input().rstrip())
data = [''] * cases

whitelist = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
for i in range(cases):
    data[i] = ''.join(filter(whitelist.__contains__, input().rstrip()))
for i in range(cases): print(data[i].rstrip())

