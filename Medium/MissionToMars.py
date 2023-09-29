cases = int(input())

values = [""] * cases
for i in range(cases):
    distance, speed = map(float, input().split(" "))
    
    time_in_seconds = round(distance * 1e6 / speed * 3600)
    days, time_in_seconds = divmod(time_in_seconds, 24 * 3600)
    hours, time_in_seconds = divmod(time_in_seconds, 3600)
    minutes, seconds = divmod(time_in_seconds, 60)
    
    values[i] = f"Time to Mars: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

for i in range(cases):
    print(values[i])