from django import forms
from . import models
from django.contrib.auth.models import User


class Profiles(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('user', 'Name', 'lastname', 'account_type')


# class Profiles(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', '', 'first_name', 'last_name', 'password']
