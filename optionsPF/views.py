from django.shortcuts import render
from django.shortcuts import HttpResponse
from .OptionsChain import *
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
            model_expiry_dates = Dates(3)
            print(model_expiry_dates)
            model_expiry_dates.save()
            return render(request, 'optionsPF/date.html')
    else:
        return render(request, 'optionsPF/home.html')


def search(request):
    if request.method == 'POST':
        user_input = request.POST.get('textfield', None)
        option_expiry_dates = get_options_expirations(user_input)
        option_chain = get_option_chain(user_input, option_expiry_dates)
        html = ("<h1>%s</h1>", option_chain)
        return HttpResponse(option_chain.to_html())
    else:
        return render(request, 'optionsPF/home.html')