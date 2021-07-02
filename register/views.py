from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from optionsPF.views import butterfly
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        contract_id = request.POST.get("contract-id")
        backlink = request.POST.get("prev-link")
        print(contract_id)
        link = request.META.get('HTTP_REFERER')
        print(link)
        split_link = str(link).split('/')[3]
        if form.is_valid():
            form.save()
        if split_link == "register":
            return butterfly(request)
        elif split_link == "home":
            redirect('/home')
    else:
        form = RegisterForm()
        return render(request, "register/register.html", {"form": form})


def register_success(request):
    print(request.POST)
    return redirect("success")


def login_success(request):
    print(request.POST)
    return redirect('portfolio-home')


def pre_login(request):
    print(request.POST)
    messages.add_message(request, messages.INFO, request.POST.get('contract-id'))
    messages.add_message(request, messages.INFO, request.POST.get('referral-link'))
    if "login-button" in request.POST:
        return redirect("login")
    else:
        return redirect("/register/")


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    print("here")

    if user is not None:
        if user.is_active:
            auth.login(request, user)
            print(request.POST)
            if "home-link" in request.POST:
                return redirect("portfolio-home")
            else:
                return butterfly(request)
    else:
        messages.info(request, "Enter a Valid Login")
        return redirect("login")
