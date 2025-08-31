from django import forms
from .models import Owner, Electronic

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'email']


class ElectronicForm(forms.ModelForm):
    class Meta:
        model = Electronic
        fields = ['name', 'type', 'owner']
