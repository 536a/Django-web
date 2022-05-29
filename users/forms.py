from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class AccountRegisterForm(UserCreationForm):

    class Meta:
        model=Account
        fields=['email','first_name','last_name']


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['picture','phone']