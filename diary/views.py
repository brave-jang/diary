import calendar
from datetime import date, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import todoForm
from .models import todoModel


def main(request):
    today = str(date.today())
    cal = today.split("-")
    year, month, day = cal[0], cal[1], cal[2]
    yesterday = date.today() - timedelta(1)
    tomorrow = date.today() + timedelta(1)
    yester_list = todoModel.objects.filter(user=request.user)\
        .filter(end_date__gte=yesterday)
    today_list = todoModel.objects.filter(user=request.user)\
        .filter(end_date__gte=date.today())
    tomorrow_list = todoModel.objects.filter(user=request.user)\
        .filter(end_date__gte=tomorrow)
    return render(request, "diary/main.html", { 
            'year':year, 'month':month, 'day':day, 'today_list':today_list,
            'yester_list':yester_list, 'tomorrow_list': tomorrow_list})


def Detailcalendar(request, year, month):
    today = str(date.today())
    cal = today.split("-")
    today_year, today_month, today_day = cal[0], cal[1], cal[2]
    month_days = calendar.monthcalendar(int(year), int(month))
    days = [0,]
    for week_days in month_days:
        for week_day in week_days:
            days.append(week_day)
    days.pop()
    return render(request, "diary/calendar.html", {'days':days, 
            'year':year, 'month':month,'today_year':today_year,
            'today_month':today_month, 'today_day':today_day})


def write_todo(request):
    today = str(date.today())
    cal = today.split("-")
    year, month, day = cal[0], cal[1], cal[2]
    todo_list = todoModel.objects.filter(user=request.user)
    if request.method == "POST":
        forms = todoForm(request.POST)
        if forms.is_valid():
            todo = forms.save(commit=False)
            if todo.start_date > todo.end_date:
                messages.error(request, "시작일이 종료일보다 늦습니다!")
                return redirect("diary:todo")
            else:
                todo.user = request.user
                forms.save()
                return redirect("diary:todo")
    else:
        forms = todoForm()
    return render(request, "diary/todo_write.html", { 
                'year':year, 'month':month, 'day':day, 'todo_list':todo_list})