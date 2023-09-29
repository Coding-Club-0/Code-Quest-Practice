cases = int(input().rstrip())

wheels = [["red-orange", "orange", "yellow-orange"], ["yellow-green", "green", "blue-green"], ["red-violet", "violet", "blue-violet"]]
results = ["red and yellow", "blue and yellow", "blue and red"]
def whichIndex(arr, color):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == color: return results[i]
    return ""

data = [''] * cases
for i in range(cases):
    color = input().rstrip()
    data[i] = [color, whichIndex(wheels, color)]

for i in range(cases):
    d = data[i]
    if len(d[1]) == 0: print(f'No colors need to be mixed to make {d[0]}.')
    else: print(f"In order to make {d[0]}, {d[1]} must be mixed.")