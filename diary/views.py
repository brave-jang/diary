import calendar
from datetime import datetime
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import todoForm, listForm
from .models import todoModel

@login_required
def main(request):
    today = str(date.today())
    cal = today.split("-")
    year, month, day = cal[0], cal[1], cal[2]
    yesterday = date.today() - timedelta(1)
    tomorrow = date.today() + timedelta(1)
    yester_list = todoModel.objects.filter(user=request.user)\
        .filter(start_date__lte=yesterday)
    today_list = todoModel.objects.filter(user=request.user)\
        .filter(end_date__gte=date.today())
    tomorrow_list = todoModel.objects.filter(user=request.user)\
        .filter(end_date__gte=tomorrow)
    return render(request, "diary/main.html", { 
            'year':year, 'month':month, 'day':day, 'today_list':today_list,
            'yester_list':yester_list, 'tomorrow_list': tomorrow_list})


@login_required
def Detailcalendar(request, year, month):
    today = str(date.today())
    cal = today.split("-")
    today_year, today_month, today_day = cal[0], cal[1], cal[2]
    month_days = calendar.monthcalendar(int(year), int(month))
    month_begin = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d")
    end = calendar.monthrange(year, month)[1]
    month_end = datetime.strptime(f"{year}-{month}-{end}", "%Y-%m-%d")
    todo_list = todoModel.objects.filter(user=request.user)\
                    .filter(end_date__gte=month_begin)\
                    .filter(end_date__lte=month_end)
    success_todo = todoModel.objects.filter(user=request.user)\
                    .filter(end_date__gte=month_begin)\
                    .filter(end_date__lte=month_end)\
                    .filter(status="T")
    try:
        success_rate = round(len(success_todo)/len(todo_list)*100, 1)
    except:
        success_rate = 0
    days = [0,]
    for week_days in month_days:
        for week_day in week_days:
            days.append(week_day)
    days.pop()
    return render(request, "diary/calendar.html", {'days':days, 
            'year':year, 'month':month,'today_year':today_year,
            'today_month':today_month, 'today_day':today_day, 'todo_list':todo_list,
            'success_todo':success_todo, 'success_rate':success_rate})


@login_required
def write_todo(request):
    today = str(date.today())
    cal = today.split("-")
    year, month, day = cal[0], cal[1], cal[2]
    todo_list = todoModel.objects.filter(user=request.user)\
        .filter(end_date__gte=date.today())
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

@login_required
def list_todo(request):
    today = str(date.today())
    cal = today.split("-")
    year, month, day = cal[0], cal[1], cal[2]
    if request.method == 'POST':
        forms = listForm(request.POST)
        if forms.is_valid():
            start_date = forms.cleaned_data.get('start_date')
            end_date = forms.cleaned_data.get('end_date')
            todo_list = todoModel.objects.filter(user=request.user)\
                        .filter(end_date__gte=start_date)\
                        .filter(end_date__lte=end_date)
    else:
        forms = listForm()
    return render(request, "diary/todo_list.html", { 
                'year':year, 'month':month, 'day':day, 'todo_list':todo_list})

@login_required
def trans_todo(request, pk):
    today = str(date.today())
    cal = today.split("-")
    year, month = cal[0], cal[1]
    todo = todoModel.objects.get(pk=pk)
    if todo.status == 'F':
        todo.status = 'T'
        todo.save()
    else:
        todo.status = 'F'
        todo.save()
    return redirect(reverse("diary:Detailcalendar", kwargs={"year":year, "month":month}))
    