from datetime import datetime, timedelta

names = ["Smith", "Sprey", "Anderson", "Bolade", "Hassan", "Agarwal", "Sato", "Thomas"]
timezone = ["America/Phoenix", "America/New_York", "Etc/Greenwich", "Africa/Lagos", "Africa/Cairo", "Indian/Antananarivo", "Asia/Tokyo", "Australia/Melbourne"]

cases = int(input().rstrip())
for i in range(cases):
    data = input().rstrip().split(" ")
    organizer = data[0]
    year, month, day = list(map(int, data[1].split("-")))
    hour, minute = list(map(int, data[2].split(":")))

