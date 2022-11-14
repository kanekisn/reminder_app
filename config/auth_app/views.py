from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            us = authenticate(request, username=username, password=password)
            if us is not None:
                if us.is_active:
                    auth_login(request, us)
                    return redirect(reverse('reminder_home'))
                else:
                    return HttpResponse("You're account is disabled.")
            else:
                return render(request = request,
                        template_name = "auth_app/login.html",
                        context={"form":form, 'error': '0'})
    else:
        form = LoginForm()

    return render(request = request,
                        template_name = "auth_app/login.html",
                        context={"form":form})
@login_required
def logout_user(request):
    logout(request)
    return render(request = request,
                        template_name = "auth_app/logout.html")
    
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user, password=password)
            auth_login(request, user)
            
            return redirect(reverse('reminder_home'))
    else:
        form = RegisterForm()

    return render(request = request,
                        template_name = "auth_app/register.html",
                        context={"form":form})