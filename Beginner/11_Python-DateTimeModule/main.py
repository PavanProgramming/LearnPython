import datetime

print('****************************')
print(dir(datetime))
print('****************************')

print(datetime.MINYEAR)
print(datetime.MAXYEAR)
# print(datetime._)

d = datetime.date(1993, 8, 28)  # 08 for month is invalid
print(d)

td = datetime.date.today()  # 08 for month is invalid
print(td)
print((td-d).total_seconds())
# print(td.weekday())  # starts monday as 0, ends sunday as 6
# print(td.isoweekday())  # starts monday as 1, ends sunday as 7

t = datetime.time(10, 10, 10, 100000)
print(t)
print(t.hour)

tdelta = datetime.timedelta(days=1)
print(td + tdelta)

dt = datetime.datetime(2023, 1, 3, 10, 1, 10)
print(dt + tdelta)

tdelta = datetime.timedelta(hours=10)
print(tdelta)
print(dt+tdelta)


# IST using time delta
dt_India = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
Indian_time = dt_India.strftime('%d-%b-%y %H:%M:%S')
print(Indian_time)

# https://docs.python.org/3/library/datetime.html

dt_today = datetime.datetime.today() # returns current local time with time zone none
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow() # Return the current UTC date and time, with tzinfo None same as datetime.datetime.now(tz=pytz.UTC)

print(dt_today)
print(dt_now)
print(dt_utcnow)

import pytz

dt = datetime.datetime(2023, 1, 3, 10, 1, 10, tzinfo=pytz.UTC)
dt_ist = dt_now.astimezone(pytz.timezone("Asia/kolkata")) # .strftime('%Y-%m-%d %H:%M:%S.%f')

# for tz in pytz.all_timezones:
#     print(tz)

ist_tz = pytz.timezone("Asia/kolkata")
dt_now = ist_tz.localize(dt_now)
print(dt_now)

print('****************************')
# strftime : datetime to string
dt_ist = datetime.datetime.now()
print(dt_ist.strftime('%B-%d,%Y'))
print(dt_ist.strftime('%b-%d, %Y'))

# strptime : String to datetime
dt_str = 'Jan-04, 2023'
dt_new = datetime.datetime.strptime(dt_str, '%b-%d, %Y') # format is string(dt_str) format
print(dt_new)

print('****************************')





