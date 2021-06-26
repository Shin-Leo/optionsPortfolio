import django
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.db.utils import IntegrityError
from .options_chain import *
from django import forms
import datetime
import pdb
import json
import uuid
from .models import *


def home(request):
    return render(request, 'optionsPF/home.html')


def about(request):
    return render(request, 'optionsPF/about.html')


def dates(request):
    if request.method == 'POST':
        user_input = request.POST.get('textfield', None)
        if ',' not in user_input:
            if len(user_input) != 0 and len(user_input) < 5:
                option_expiry_dates = get_options_expirations(user_input)
                print(option_expiry_dates)
                if option_expiry_dates:
                    option_expiry_dates_list = list(option_expiry_dates)
                    context = {'option_expiry_dates_list': option_expiry_dates_list,
                               'ticker': user_input, 'strategies': options_strategies}
                    return render(request, 'optionsPF/date.html', context)
            else:
                messages.info(request, "Enter a Valid Stock Ticker")
                return render(request, 'optionsPF/home.html')
        else:
            messages.info(request, "Enter a Single Stock Ticker")
            return render(request, 'optionsPF/home.html')
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
        if strategy == 'Butterfly':
            return render(request, 'optionsPF/butterfly.html', context)
        else:
            return render(request, 'optionsPF/date.html')
    else:
        return render(request, 'optionsPF/home.html')


def butterfly(request):
    referrer_link = request.META.get('HTTP_REFERER')
    split_link = str(referrer_link).split('/')[3]
    print(split_link)
    if request.method == 'POST' and split_link != 'login':
        strike = request.POST.get('strike-price')
        last_price = request.POST.get('last-price')
        strategy = request.POST.get('selected-strategy')
        ticker = request.POST.get('selected-ticker')
        num_contracts = 1
        expiry_date = request.POST.get('selected-expiry')
        eastern = timezone('US/Eastern')
        purchase_date = datetime.datetime.now(tz=eastern).date()

        contract = ButterflySpread.objects.create(strike=strike, contract_price=last_price, purchase_date=purchase_date,
                                                  expiry_date=expiry_date, num_contracts=num_contracts, ticker=ticker,
                                                  strategy_name=strategy)
        contract.save()
        contract_attributes = contract.return_attributes()
        contract_attributes.update({'backLink': split_link})
        print(contract_attributes)
        return render(request, 'optionsPF/success.html', contract_attributes)
    elif split_link == 'login':
        contract_id = request.POST.get('contract-id')
        contract = ButterflySpread.objects.get(pk=contract_id)
        attributes = contract.return_attributes()
        return render(request, 'optionsPF/success.html', attributes)
    else:
        return render(request, 'optionsPF/home.html')


class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return str(z)
        else:
            return super().default(z)


def portfolio(request):
    if request.method == 'POST':
        contract_id = request.POST.get('contract-id')
        user_id = uuid.uuid4()
        string_id = user_id.__str__()
        contract = ButterflySpread.objects.get(pk=contract_id)
        contract_attributes = contract.return_attributes()
        contract_attributes['contract_price'] = float(contract_attributes['contract_price'])
        unique_contract_attributes = {string_id: contract_attributes}
        json_attributes = json.dumps(unique_contract_attributes, cls=DateTimeEncoder)
        try:
            user_portfolio = Portfolio.objects.create(user=request.user, strategies=json_attributes)
            user_portfolio.save()
            user_portfolio_strategies = user_portfolio.strategies
            print(user_portfolio_strategies)
            contract_details = json.loads(user_portfolio_strategies[string_id])
            return render(request, 'optionsPF/portfolio.html', contract_details)
        except IntegrityError or AttributeError:
            retrieved_portfolio = Portfolio.objects.get(pk=request.user)
            existing_strategies = eval(retrieved_portfolio.strategies)
            existing_strategies.update(unique_contract_attributes)
            json_attributes = json.dumps(existing_strategies, cls=DateTimeEncoder)
            retrieved_portfolio.strategies = json_attributes
            retrieved_portfolio.save()
            print(existing_strategies)
            for key, value in list(existing_strategies.items()):
                print(key)
                print(value)
                for k, v in list(value.items()):
                    if k == 'id':
                        value.pop(k)
            contract_details = {"contract": existing_strategies}
            return render(request, 'optionsPF/portfolio.html', contract_details)

