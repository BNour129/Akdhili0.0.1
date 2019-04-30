from django import forms
from . import models

class AccountDetails(forms.ModelForm):
    class Meta:
        model = models.AccountDetail
        fields = ['Name', 'lastname', 'account_type', 'cin', 'picture']
