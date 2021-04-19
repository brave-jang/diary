import calendar
from datetime import date
from django.shortcuts import render


def main(request):
    month_days = calendar.monthcalendar(2021, 4)
    days = [0,]
    for week_days in month_days:
        for week_day in week_days:
            days.append(week_day)
    print(date.today())
    return render(request, "diary/main.html", {'days':days})