from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    path('search/', views.search, name='portfolio-search'),
    path('dates/', views.dates, name='portfolio-dates'),
    path('covered_call/', views.covered_call, name='portfolio-covered-call'),
    url(r'^covered_call$', views.covered_call, name='get-covered-call'),
]
