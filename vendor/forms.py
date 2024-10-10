from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'GSTIN', 'address', 'email', 'phone', 'item_offered']
