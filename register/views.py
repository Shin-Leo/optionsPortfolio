from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from optionsPF.views import butterfly
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        redirect('/home')
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


def login_success(request):
    print(request.POST)
    return redirect('portfolio-home')


def pre_login(request):
    messages.add_message(request, messages.INFO, request.POST.get('contract-id'))
    messages.add_message(request, messages.INFO, request.POST.get('referral-link'))
    return redirect("login")


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    referrer_link = request.POST.get('prev-link')
    split_link = str(referrer_link).split('/')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth.login(request, user)
            if split_link == "home":
                return redirect("portfolio-home")
            else:
                return butterfly(request)
    else:
        return HttpResponseRedirect("Invalid username or password")
