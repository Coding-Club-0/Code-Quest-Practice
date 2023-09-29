from datetime import *

cases = int(input().rstrip())
for i in range(cases):
    day, t, offset = input().rstrip().split(" ")
    month, day, year = list(map(int, day.split("/")))
    hour, minute = list(map(int, t.split(":")))
    offset = float(offset)

    delta = datetime(year, month, day, hour, minute) - timedelta(hours=offset)
    day2, time2 = str(delta).split(" ")
    year2, month2, day2 = day2.split("-")
    hour2, min2, sec2 = time2.split(":")
    print(f'{month2}/{day2}/{year2} {hour2}:{min2}')