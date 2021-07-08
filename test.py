from datetime import date, timedelta
import datetime
import calendar

today = datetime.date.today()

last = today.replace(day=calendar.monthrange(today.year, today.month)[1])

if last.weekday() < 5:
    print(last)

else:
    print(last - timedelta(days=1 + last.weekday() - 5))
    print("test")
