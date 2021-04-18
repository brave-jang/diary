from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import LoginForms

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
        return render(request, "accounts/login.html")