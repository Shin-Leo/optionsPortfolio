from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    path('search/', views.search, name='portfolio-search'),
]
