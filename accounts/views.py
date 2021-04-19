from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import LoginForms, SignupForm

def Login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect("diary:main")
        else:
            return render(request, "accounts/Login.html", {'form':form})
    else:
        form = LoginForms()
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