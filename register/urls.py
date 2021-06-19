from django.conf.urls import url
from django.urls import path
from . import views
import optionsPF.views
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import cache_control
from django.conf import settings

urlpatterns = [
    path('home/', optionsPF.views.home, name='portfolio-home'),
    url(r'login_success/$', views.login_success, name='login_success'),
    url(r'^/accounts/auth/$', 'auth_view'),
]
