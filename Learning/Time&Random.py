import datetime
import time
import random

print(time.time())
print(time.clock())
print(time.gmtime())
print(time.localtime())

print(help(time.strftime))

localTime = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', localTime))
print(time.strptime('2018-01-06 20:52:10', '%Y-%m-%d %H:%M:%S'))
# time.struct_time(tm_year=2018, tm_mon=1, tm_mday=6, tm_hour=20, tm_min=52, tm_sec=10, tm_wday=5, tm_yday=6, tm_isdst=-1)
print(time.strptime('2018-01-06 20:52:10', '%Y-%m-%d %H:%M:%S').tm_mon)

print(time.ctime())
print(time.ctime(1515243488.7232044))
print(time.mktime(time.localtime()))

print(datetime.datetime.now())

print(random.random())      # [0, 1)
print(random.randint(1, 4))     # 1, 2, 3, 4
print(random.randrange(1, 4))       # 1, 2, 3, differ from above
print(random.choice('Lory'))
print(random.choice(['Lory', 98, (1, 2), [4, 5]]))
print(random.sample(['Lory', 98, (1, 2), [4, 5]], 2))

print(chr(65))      # Return A
