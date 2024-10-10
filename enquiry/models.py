from django.db import models

class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('Organizational', 'Organizational'),
        ('Private', 'Private'),
    ]
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    make = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField()
    lead_time = models.IntegerField(help_text="Lead time in days")
    
    def __str__(self):
        return self.name

class Enquiry(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Pending")
    
    def __str__(self):
        return f"Enquiry {self.enquiry_id} - {self.customer.name}"
