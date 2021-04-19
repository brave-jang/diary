from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import LoginForms, SignupForm

def Login(request):
    if request.method == 'POST':
        user = LoginForms(request.POST)
        if user.is_valid():
            username = user.cleaned_data['username']
            password = user.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect("diary:main")
        else:
            messages.error(request, "아이디가 존재하지 않거나 패스워드가 틀립니다!")
            return render(request, "accounts/Login.html")
    else:
        return render(request, "accounts/Login.html")


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect("diary:main")
        else:
            return render(request, "accounts/Signup.html", {'form':form})
    else:
        form = SignupForm()
    return render(request, "accounts/Signup.html", {'form':form})