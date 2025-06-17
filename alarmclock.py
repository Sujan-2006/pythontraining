import datetime

date = datetime.date(2006, 3, 3)
today=datetime.date.today()
time=datetime.time(12, 35, 9)
now=datetime.datetime.now()
now=now.strftime("%H:%M:%S %m-%d-%Y")

print(date)
print(today)
print(time)
print(now)

target_datetime=datetime.datetime(2030, 3, 3, 12, 40, 5)
current_datetime=datetime.datetime.now()

if target_datetime<current_datetime:
    print("Target date has already passed")
else:
    print("Target date has not passed")