from django.conf.urls import url
from django.urls import path
from optionsPF import views
from django.conf.urls.static import static
from register import views as v
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control
from django.conf import settings

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    path('strategies/', views.strategies, name='portfolio-strategies'),
    path('dates/', views.dates, name='portfolio-dates'),
    path('butterfly/', views.butterfly, name='portfolio-butterfly'),
    path('portfolio/', views.portfolio, name='portfolio-user'),
    path('pre_login/', v.pre_login, name='register-pre-login'),
    path('strategy/', views.strategy, name='portfolio-strategy'),
    path('search/', views.search, name='portfolio-search'),
    url(r'^butterfly$', views.butterfly, name='get-butterfly'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))
