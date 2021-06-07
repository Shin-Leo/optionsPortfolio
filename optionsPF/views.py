from django.shortcuts import render
from django.shortcuts import HttpResponse
from .OptionsChain import get_option_chain


def home(request):
    return render(request, 'optionsPF/home.html')


def about(request):
    return render(request, 'optionsPF/about.html')


def search(request):
    if request.method == 'POST':
        user_input = request.POST.get('textfield', None)
        option_chain = get_option_chain(user_input)
        html = ("<h1>%s</h1>", option_chain)
        return HttpResponse(option_chain.to_html())
    else:
        return render(request, 'optionsPF/home.html')
