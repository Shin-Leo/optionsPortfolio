import django
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.db.utils import IntegrityError
from .options_chain import *
from django import forms
import datetime as dt
from datetime import datetime
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
                               'ticker': user_input.upper(), 'strategies': options_strategies}
                    return render(request, 'optionsPF/date.html', context)
            else:
                messages.info(request, "Enter a Valid Stock Ticker")
                return render(request, 'optionsPF/home.html')
        else:
            messages.info(request, "Enter a Single Stock Ticker")
            return render(request, 'optionsPF/home.html')
    else:
        return render(request, 'optionsPF/home.html')


def strategies(request):
    if request.method == 'POST':
        ticker = request.POST.get('textfield', None)
        date = request.POST.get('selected-date', None)
        context = {"ticker": ticker,
                   "date": date}
        return render(request, 'optionsPF/strategies.html', context)
        # option_chain = get_option_chain(ticker, date)
        # stock_price = str(get_stock_price(ticker)).replace("[", "").replace("]", "")
        # context = {'calls': option_chain[0], 'puts': option_chain[1],
        #            'strategies': option_chain[2], 'price': stock_price,
        #            'strategy': strategy, 'ticker': ticker, 'date': date}
        # if strategy == 'Butterfly':
        #     return render(request, 'optionsPF/butterfly.html', context)
        # elif strategy == 'Iron-Condor':
        #     return render(request, 'optionsPF/iron_condor.html', context)
        # else:
        #     return render(request, 'optionsPF/date.html')
    else:
        return render(request, 'optionsPF/home.html')


def search(request):
    if request.method == 'POST':
        ticker = request.POST.get('selected-ticker')
        date = request.POST.get('selected-expiry')
        option_chain = get_option_chain(ticker, date)
        stock_price = str(get_stock_price(ticker)).replace("[", "").replace("]", "")
        context = {'calls': option_chain[0], 'puts': option_chain[1],
                   'strategies': option_chain[2], 'price': stock_price,
                   'strategy': strategy, 'ticker': ticker, 'date': date}
        if "butterfly-button" in request.POST:
            return render(request, 'optionsPF/butterfly.html', context)
        elif "condor-button" in request.POST:
            return render(request, 'optionsPF/iron_condor.html', context)
        else:
            return render(request, 'optionsPF/date.html')
    else:
        return render(request, 'optionsPF/home.html')


def butterfly(request):
    referrer_link = request.META.get('HTTP_REFERER')
    split_link = str(referrer_link).split('/')[3]
    if request.method == 'POST' and split_link == 'search':
        lower_strike = request.POST.get('low-strike')
        midpoint_strike = request.POST.get('mid-strike')
        upper_strike = request.POST.get('high-strike')
        lower_contract_price = request.POST.get('low_contract_price')
        midpoint_contract_price = request.POST.get('mid_contract_price')
        upper_contract_price = request.POST.get('high_contract_price')
        strategy_price = 0
        ticker = request.POST.get('selected-ticker')
        selected_strategy = request.POST.get('selected-butterfly')
        num_contracts = request.POST.get('num-contracts')
        expiry_date = request.POST.get('selected-expiry')
        eastern = timezone('US/Eastern')
        purchase_date = dt.datetime.now(tz=eastern).date()
        collapsible_tag = create_collapsible_button_tag(expiry_date, lower_strike, midpoint_strike, upper_strike,
                                                        selected_strategy)
        contract = ButterflySpread.objects.create(lower_bound_strike=lower_strike, midpoint_strike=midpoint_strike,
                                                  upper_bound_strike=upper_strike,
                                                  low_strike_contract_price=lower_contract_price,
                                                  mid_strike_contract_price=midpoint_contract_price,
                                                  high_strike_contract_price=upper_contract_price,
                                                  current_low_strike_contract_price=lower_contract_price,
                                                  current_mid_strike_contract_price=midpoint_contract_price,
                                                  current_high_strike_contract_price=upper_contract_price,
                                                  current_strategy_price=strategy_price, strategy_price=strategy_price,
                                                  purchase_date=purchase_date, expiry_date=expiry_date,
                                                  num_contracts=num_contracts, ticker=ticker,
                                                  collapsible_tag=collapsible_tag,
                                                  strategy_name=selected_strategy)
        contract.save()
        contract_attributes = contract.return_attributes()
        contract_attributes.update({'backLink': split_link})
        return render(request, 'optionsPF/success.html', contract_attributes)
    elif split_link == 'login' or split_link == "register":
        contract_id = request.POST.get('contract-id')
        contract = ButterflySpread.objects.get(pk=contract_id)
        attributes = contract.return_attributes()
        collapsible_tag = create_collapsible_button_tag(attributes["expiry_date"], attributes["lower_strike"],
                                                        attributes["midpoint_strike"],
                                                        attributes["upper_strike"],
                                                        attributes["strategy"])
        attributes.update({'collapsible_tag': collapsible_tag})
        ButterflySpread.objects.filter(pk=contract_id).update(collapsible_tag=collapsible_tag)

        if split_link == "register":
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
        return render(request, 'optionsPF/success.html', attributes)
    else:
        return render(request, 'optionsPF/home.html')


def create_collapsible_button_tag(date, low, mid, high, strategy):
    if type(date) == str:
        datetime_obj = datetime.strptime(str(date) + " 00:00:00", '%Y-%m-%d %H:%M:%S')
        month = datetime_obj.strftime("%B")
    else:
        month = date.strftime("%B")
    return month + f" {low}:{mid}:{high} " + strategy


class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, dt.datetime):
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
        contract_attributes['low_strike_contract_price'] = float(contract_attributes['low_strike_contract_price'])
        contract_attributes['mid_strike_contract_price'] = float(contract_attributes['mid_strike_contract_price'])
        contract_attributes['high_strike_contract_price'] = float(contract_attributes['high_strike_contract_price'])
        contract_attributes['strategy_price'] = float(contract_attributes['strategy_price'])
        contract_attributes['current_low_strike_contract_price'] = 1
        contract_attributes['current_mid_strike_contract_price'] = 1
        contract_attributes['current_high_strike_contract_price'] = 1
        contract_attributes['current_strategy_price'] = 1

        unique_contract_attributes = {string_id: contract_attributes}
        json_attributes = json.dumps(unique_contract_attributes, cls=DateTimeEncoder)
        options_chain = get_option_chain(contract_attributes['ticker'],
                                         contract_attributes['expiry_date'].date().strftime("%Y-%m-%d"))
        low_contract_price = 0
        mid_contract_price = 0
        high_contract_price = 0
        for calls in options_chain:
            for row in calls:
                if row[0] == contract_attributes['low_strike_contract_price']:
                    low_contract_price = row[1]
                elif row[0] == contract_attributes['mid_strike_contract_price']:
                    mid_contract_price = row[1]
                elif row[0] == contract_attributes['high_strike_contract_price']:
                    high_contract_price = row[1]

        context = retrieve_butterfly_contracts(unique_contract_attributes)
        try:
            user_portfolio = Portfolio.objects.create(user=request.user, strategies=json_attributes)
            user_portfolio.save()
            return render(request, 'optionsPF/portfolio.html', {"context": context})
        except IntegrityError or AttributeError:
            retrieved_portfolio = Portfolio.objects.get(pk=request.user)
            if retrieved_portfolio.strategies != {}:
                existing_strategies = eval(retrieved_portfolio.strategies)
                existing_strategies[list(unique_contract_attributes.keys())[0]] = \
                    list(unique_contract_attributes.values())[0]
                json_attributes = json.dumps(existing_strategies, cls=DateTimeEncoder)
                retrieved_portfolio.strategies = json_attributes
                context = retrieve_butterfly_contracts(existing_strategies)
            else:
                retrieved_portfolio.strategies = json.dumps(unique_contract_attributes, cls=DateTimeEncoder)
            retrieved_portfolio.save()
            return render(request, 'optionsPF/portfolio.html', {"context": context})
    else:
        if request.user.is_authenticated:
            try:
                user_portfolio = Portfolio.objects.create(user=request.user, strategies={})
                user_portfolio.save()
                return render(request, 'optionsPF/portfolio.html')
            except IntegrityError or TypeError:
                retrieved_portfolio = Portfolio.objects.get(pk=request.user)
                if retrieved_portfolio.strategies != {}:
                    existing_strategies = eval(retrieved_portfolio.strategies)
                    json_attributes = json.dumps(existing_strategies, cls=DateTimeEncoder)
                    retrieved_portfolio.strategies = json_attributes
                    retrieved_portfolio.save()
                    context = retrieve_butterfly_contracts(existing_strategies)

                    for key, value in context.items():
                        ticker = value[0]["ticker"]
                        date = value[0]["expiry_date"]
                        # add exception for if the current date is after expiry date
                        try:
                            options_chain = get_option_chain(ticker,
                                                             date.strftime("%Y-%m-%d"))
                            low_contract_price = 0
                            mid_contract_price = 0
                            high_contract_price = 0
                            for calls in options_chain:
                                for row in calls:
                                    if row[0] == value[0]['low_strike_contract_price']:
                                        low_contract_price = row[1]
                                    elif row[0] == value[1]['mid_strike_contract_price']:
                                        mid_contract_price = row[1]
                                    elif row[0] == value[2]['high_strike_contract_price']:
                                        high_contract_price = row[1]
                            value[0]["current_low_strike_contract_price"] = low_contract_price
                            value[1]["current_mid_strike_contract_price"] = mid_contract_price
                            value[2]["current_high_strike_contract_price"] = high_contract_price
                        except ValueError:
                            del context[key]
                            break
                    return render(request, 'optionsPF/portfolio.html', {"context": context})
                else:
                    return render(request, 'optionsPF/portfolio.html')


def retrieve_butterfly_contracts(strategies):
    context = {}
    for key, value in strategies.items():
        for k, v in value.items():
            if k == 'id':
                butterfly_object = ButterflySpread.objects.get(pk=v)
                low_contract = butterfly_object.return_low_leg()
                mid_contract = butterfly_object.return_middle_leg()
                high_contract = butterfly_object.return_high_leg()

                get_option_chain(ticker=low_contract['ticker'], date=str(low_contract["expiry_date"]))
                current_low_strike_contract_price = low_contract.pop("current_low_strike_contract_price")
                print(current_low_strike_contract_price - low_contract["low_strike_contract_price"])
                current_mid_strike_contract_price = mid_contract.pop("current_mid_strike_contract_price")
                current_high_strike_contract_price = high_contract.pop("current_high_strike_contract_price")
                low_contract["Contract Value"] = '$' + str(float((current_low_strike_contract_price
                                                                  * low_contract['contract_size'])) * 100)
                mid_contract["Contract Value"] = '$' + str(float((current_mid_strike_contract_price
                                                                  * mid_contract['contract_size'])) * 100)
                high_contract["Contract Value"] = '$' + str((float((current_high_strike_contract_price
                                                                    * high_contract['contract_size']))) * 100)
                low_contract["low_percentage_change"] = (current_low_strike_contract_price - low_contract[
                    "low_strike_contract_price"]) / low_contract["low_strike_contract_price"]
                mid_contract["mid_percentage_change"] = (current_mid_strike_contract_price - mid_contract[
                    "mid_strike_contract_price"]) / mid_contract["mid_strike_contract_price"]
                high_contract["high_percentage_change"] = (current_high_strike_contract_price - high_contract[
                    "high_strike_contract_price"]) / high_contract["high_strike_contract_price"]
                tag = butterfly_object.return_collapsible_tag()
                print(mid_contract["mid_percentage_change"])
                context.update({tag: [low_contract, mid_contract, high_contract]})
                break
    return context


def strategy(request):
    return render(request, 'optionsPF/strategies.html')
