import datetime

year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))

x = datetime.datetime.now()
y = datetime.datetime(year, month, day)
res = x - y
print(x)
print(y)
print(res[day])

