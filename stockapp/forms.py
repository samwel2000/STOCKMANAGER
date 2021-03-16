from django import forms
from .models import *
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['language']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_date','created_by']
        widgets = {'description':forms.Textarea()}

class ExistingProductForm(forms.ModelForm):
    class Meta:
        model = ProductPurchase
        exclude = ['created_date','created_by']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Requests
        exclude = [
                'requested_by',
                'request_status',
                'approved_date',
                'returned_date',
                'requested_date'
                ]
