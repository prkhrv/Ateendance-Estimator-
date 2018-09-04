from django import forms
from myapp.models import checkdata


class calculate(forms.ModelForm):


    class Meta():
        model = checkdata
        fields = ('a',
                  'b',
                  'c',
                  'd',
                  'e',)
