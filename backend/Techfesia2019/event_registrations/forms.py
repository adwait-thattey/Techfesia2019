from django import forms
from django.forms.widgets import PasswordInput


class StaffLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=PasswordInput)
