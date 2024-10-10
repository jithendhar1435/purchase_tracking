from django.shortcuts import render, redirect
from .forms import CustomerForm, ItemForm, EnquiryForm
from .models import Customer, Item, Enquiry

def create_enquiry(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        item_form = ItemForm(request.POST)
        enquiry_form = EnquiryForm(request.POST)
        if customer_form.is_valid() and item_form.is_valid() and enquiry_form.is_valid():
            customer = customer_form.save()
            item = item_form.save()
            enquiry = enquiry_form.save(commit=False)
            enquiry.customer = customer
            enquiry.item = item
            enquiry.save()
            return redirect('enquiry_list')
    else:
        customer_form = CustomerForm()
        item_form = ItemForm()
        enquiry_form = EnquiryForm()
    return render(request, 'enquiry/create_enquiry.html', {
        'customer_form': customer_form,
        'item_form': item_form,
        'enquiry_form': enquiry_form
    })

def enquiry_list(request):
    enquiries = Enquiry.objects.all()
    return render(request, 'enquiry/enquiry_list.html', {'enquiries': enquiries})
