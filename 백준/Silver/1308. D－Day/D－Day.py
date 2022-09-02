import datetime

year, month, day = map(int, input().split())
start = datetime.datetime(year, month, day)

year, month, day = map(int, input().split())
end = datetime.datetime(year, month, day)

if end.year - start.year == 1000:
    if end.month < start.month:
        day = str("D-") + str(end - start).split()[0]
        print(day)
    else:
        if end.day < start.day:
            day = str("D-") + str(end - start).split()[0]
            print(day)
        else:
            print("gg")
elif end.year - start.year > 1000:
    print("gg")
else:
    day = str("D-") + str(end - start).split()[0]
    print(day)