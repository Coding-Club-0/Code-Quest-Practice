cases = int(input().rstrip())

years = ["Yang", "Yin"]
elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

data = [0] * cases
for i in range(cases):
    data[i] = int(input().rstrip())

for i in range(cases):
    y = data[i]
    year = years[y % 2]
    element = elements[int(((y - 4) % 10) // 2)]
    animal = animals[(y - 4) % 12]
    print(f"{y} {year} {element} {animal}")