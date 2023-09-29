cases = int(input().rstrip())

data = [0] * cases
for i in range(cases):
    temp, water, field, orbit = input().rstrip().split(" ")
    temp = float(temp)
    orbit = float(orbit)
    water = water == "true"
    field = field == "true"

    if temp > 100: data[i] = "The planet is too hot."
    elif temp < 0: data[i] = "The planet is too cold."
    elif not water: data[i] = "The planet has no water."
    elif not field: data[i] = "The planet has no magnetic field."
    elif orbit > 0.6: data[i] = "The planet's orbit is not ideal."
    else: data[i] = "The planet is habitable."

for i in range(cases): print(data[i])