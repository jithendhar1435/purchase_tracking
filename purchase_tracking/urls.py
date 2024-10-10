# purchase_tracking/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Add this line for the homepage
    path('admin/', admin.site.urls),
    path('enquiry/', include('enquiry.urls')),
    path('vendor/', include('vendor.urls')),
]
