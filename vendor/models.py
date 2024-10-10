from django.db import models
from enquiry.models import Item  

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    GSTIN = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    item_offered = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
