from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control
from django.conf import settings

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    path('search/', views.search, name='portfolio-search'),
    path('dates/', views.dates, name='portfolio-dates'),
    path('covered_call/', views.covered_call, name='portfolio-covered-call'),
    url(r'^covered_call$', views.covered_call, name='get-covered-call'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))
