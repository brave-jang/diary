import calendar
from datetime import date
from django.shortcuts import render


def main(request):
    today = str(date.today())
    cal = today.split("-")
    year, month, day = cal[0], cal[1], cal[2]
    month_days = calendar.monthcalendar(int(year), int(month))
    days = [0,]
    for week_days in month_days:
        for week_day in week_days:
            days.append(week_day)
    days.pop()
    return render(request, "diary/main.html", {'days':days, 
            'year':year, 'month':month, 'day':day})


def add_month(request, year, month):
    month_days = calendar.monthcalendar(int(year), int(month))
    days = [0,]
    for week_days in month_days:
        for week_day in week_days:
            days.append(week_day)
    days.pop()
    return render(request, "diary/main.html", {'days':days, 
            'year':year, 'month':month,})


def write_diary(request):
    return render(request, "diary/write.html")