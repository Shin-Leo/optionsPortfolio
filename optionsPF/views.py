from django.shortcuts import render


def home(request):
    return render(request, 'optionsPF/home.html')


def about(request):
    return render(request, 'optionsPF/about.html')
