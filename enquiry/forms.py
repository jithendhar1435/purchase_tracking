from django import forms
from .models import Customer, Item, Enquiry

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'email', 'phone', 'customer_type']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'make', 'quantity', 'lead_time']

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['customer', 'item']
