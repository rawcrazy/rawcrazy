import datetime
from datetime import date
import calender
day,mnth,year=input().split('-')
date=datetime.date(year,mnth,day)
print(date.strftime("%A"))
print(calender.monthrange(year,mnth)[1],"days")
