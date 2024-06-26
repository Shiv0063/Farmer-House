from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class PartyModel(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True)
    PartyName = models.CharField(max_length=100)
    Number = models.CharField(max_length=100, null=True, blank=True)
    Address = models.TextField() 
    GSTNo = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)

class CategoryModel(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True)
    Category = models.CharField(max_length=100)

class DeliveryBoyModel(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True)
    Name = models.CharField(max_length=100)
    Number = models.CharField(max_length=100, null=True, blank=True)
    Address = models.TextField()
    Licence = models.FileField(upload_to='DeliveryBoy',null=True, blank=True)
    AdharCard = models.FileField(upload_to='DeliveryBoy',null=True, blank=True)
    PanCard = models.FileField(upload_to='DeliveryBoy',null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    PassWord = models.CharField(max_length=100, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.Licence.delete()
        self.AdharCard.delete()
        self.PanCard.delete()
        super().delete(*args, **kwargs)

class ProductModel(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True)
    ProductName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100,null=True, blank=True)
    Tax = models.CharField(max_length=100)
    Unit = models.CharField(max_length=100)
    PurchasePrice = models.CharField(max_length=100)
    MRP = models.CharField(max_length=100)
    SalsePrice = models.CharField(max_length=100)
    MinQty = models.CharField(max_length=100,blank=True)
    MaxQty = models.CharField(max_length=100,blank=True)
    BarcodeNo = models.CharField(max_length=100,blank=True)


class UserDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    Address = models.TextField()
    @property
    def email(self):
        return self.user.email
    
    @property
    def username(self):
        return self.user.username
    
class PurchaseEntryModel(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True)
    TypeofPurchase = models.CharField(max_length=100)
    BillNo = models.CharField(max_length=100)
    InvoiceNo = models.CharField(max_length=100)
    DateTime = models.DateTimeField(default=datetime.now())
    TypeofPayment = models.CharField(max_length=100)
    PartyName = models.CharField(max_length=100)
    ProductId = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Amount = models.CharField(max_length=100)

    def date(self):
        return self.DateTime.strftime('%B %d %Y')
    
class SalesEntryModel(models.Model):
    user = models.CharField(max_length=100,null=True, blank=True)
    DeliveryBoyName = models.CharField(max_length=100,null=True, blank=True)
    TypeOfBusiness = models.CharField(max_length=100,null=True, blank=True)
    DeliveryTime = models.TimeField()
    InvoiceNo = models.CharField(max_length=100,null=True, blank=True)
    DateTime = models.DateTimeField(default=datetime.now())
    PartyName = models.CharField(max_length=100,null=True, blank=True)
    ProductId = models.CharField(max_length=100,null=True, blank=True)
    Type = models.CharField(max_length=100,null=True, blank=True)
    Amount = models.CharField(max_length=100,null=True, blank=True)

    def date(self):
        return self.DateTime.strftime('%B %d %Y')

class StockModel(models.Model):
    ProductId = models.CharField(max_length=100,null=True,blank=True)
    user = models.CharField(max_length=100,null=True, blank=True)
    type = models.CharField(max_length=100,null=True, blank=True)
    ProductName = models.CharField(max_length=100,null=True, blank=True)
    Category = models.CharField(max_length=100,null=True, blank=True)
    Tax = models.CharField(max_length=100,null=True, blank=True)
    Unit = models.CharField(max_length=100,null=True, blank=True)
    PurchasePrice = models.CharField(max_length=100,null=True, blank=True)
    MRP = models.CharField(max_length=100,null=True, blank=True)
    MinQty = models.CharField(max_length=100,blank=True)
    MaxQty = models.CharField(max_length=100,blank=True)
    BarcodeNo = models.CharField(max_length=100,blank=True)
    Quantity = models.CharField(max_length=100,blank=True)
    Amount = models.CharField(max_length=100,null=True, blank=True)

class NMModel(models.Model):
    ProductId = models.CharField(max_length=100,null=True,blank=True)
    user = models.CharField(max_length=100,null=True, blank=True)
    type = models.CharField(max_length=100,null=True, blank=True)