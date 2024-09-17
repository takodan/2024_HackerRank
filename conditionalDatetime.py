import datetime

returnedDMY = list(map(int, input().rstrip().split()))

dueDMY = list(map(int, input().rstrip().split()))

returned_date = datetime.datetime(returnedDMY[2], returnedDMY[1], returnedDMY[0])
due_date = datetime.datetime(dueDMY[2], dueDMY[1], dueDMY[0])

days_late = returned_date - due_date

if days_late.days <= 0:
    print(0)
elif days_late.days < 30:
    print(days_late.days*15)
elif days_late.days < 365:
    print(round(days_late.days/30)*500)
else:
    print(10000)