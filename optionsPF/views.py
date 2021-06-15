from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .options_chain import *
from django import forms
import pdb
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
            context = {'option_expiry_dates_list': option_expiry_dates_list,
                       'ticker': user_input, 'strategies': options_strategies}
            return render(request, 'optionsPF/date.html', context)
    else:
        return render(request, 'optionsPF/home.html')


def search(request):
    if request.method == 'POST':
        ticker = request.POST.get('textfield', None)
        date = request.POST.get('selected-date', None)
        strategy = request.POST.get('selected-strategy', None)
        strategy = strategy.replace(" ", "-")
        option_chain = get_option_chain(ticker, date)
        print(get_stock_price(ticker))
        stock_price = str(get_stock_price(ticker)).replace("[", "").replace("]", "")
        context = {'calls': option_chain[0], 'puts': option_chain[1],
                   'strategies': option_chain[2], 'price': stock_price,
                   'strategy': strategy, 'ticker': ticker, 'date': date}
        if strategy == 'Covered-Call':
            return render(request, 'optionsPF/covered_call.html', context)
        else:
            return render(request, 'optionsPF/date.html')
    else:
        return render(request, 'optionsPF/home.html')


def covered_call(request):
    if request.method == 'POST':
        print(request.POST)
        strike = request.POST.get('strike-price')
        last_price = request.POST.get('last-price')
        strategy = request.POST.get('selected-strategy')
        ticker = request.POST.get('selected-ticker')
        num_contracts = 1
        date = request.POST.get('selected-expiry')
        contract = CoveredCall.objects.create(strike=strike, contract_price=last_price, expiry_date=date,
                                              num_contracts=num_contracts, ticker=ticker, strategy_name=strategy)
        print(contract)
        return HttpResponse('')
    else:
        return render(request, 'optionsPF/covered_call.html')


