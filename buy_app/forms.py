from django import forms
from .models import BuyAddress

class BuyForm(forms.ModelForm):
    class Meta:
        model = BuyAddress
        fields = ['full_name', 'address', 'city', 'phone', 'state', 'postal_code']
        exclude = ['user']
        