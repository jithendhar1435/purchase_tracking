from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_enquiry, name='create_enquiry'),
    path('list/', views.enquiry_list, name='enquiry_list'),
]
