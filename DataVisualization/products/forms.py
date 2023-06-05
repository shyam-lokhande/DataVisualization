from django import forms
from .models import *

class PurchaseForm(forms.ModelForm):
    # product=forms.ModelChoiceField(queryset=Product.objects.all(),
    #                                label='Product',
    #                                widget=forms.Select(attrs={'class':'col-6 m-2'}))
    class Meta:
        model=Purchase
        fields=['product','price','quantity']