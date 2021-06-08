from django.forms import ModelForm
from models import *


class MyModelForm(ModelForm):
    class Meta:
        model = Dates
        fields = ['date']