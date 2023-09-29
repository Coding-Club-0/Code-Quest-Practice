cases = int(input().rstrip())
for i in range(cases):
    num, method, places = input().rstrip().split(" ")
    num = float(num)
    places = int(places)

    num *= 10 ** (places)
    num = int(num)
    num /= 10 ** abs(places)
    print(num)