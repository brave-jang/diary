from django.shortcuts import render


def Login(request):
    return render(request, "accounts/login.html")