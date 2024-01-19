# surveys/forms.py
from django import forms
from .models import Response

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'birthdate', 'about_yourself']
