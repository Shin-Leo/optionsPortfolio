from django.shortcuts import render
from django.shortcuts import HttpResponse
from .OptionsChain import *
from django import forms
from .models import *


def home(request):
    return render(request, 'optionsPF/home.html')


def about(request):
    return render(request, 'optionsPF/about.html')


def dates(request):
    if request.method == 'POST':
        user_input = request.POST.get('textfield', None)
        option_expiry_dates = get_options_expirations(user_input)
        if option_expiry_dates:
            option_expiry_dates_list = list(option_expiry_dates)
            context = {'option_expiry_dates_list': option_expiry_dates_list, 'ticker': user_input}
            return render(request, 'optionsPF/date.html', context)
    else:
        return render(request, 'optionsPF/home.html')


def search(request):
    if request.method == 'POST':
        ticker = request.POST.get('textfield', None)
        date = request.POST.get('selected-date', None)
        option_chain = get_option_chain(ticker, date)
        return HttpResponse(option_chain.to_html())
    else:
        return render(request, 'optionsPF/home.html')
