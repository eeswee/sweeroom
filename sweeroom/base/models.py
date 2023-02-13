from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Client(models.Model):
    client_choices = (('self_s','small_sales'),('dist','distributor'),
                       ('brand','brand_sales'),('cust','end_user'),('fac','factory'))
    name = models.CharField('Client Company', max_length=200)
    type = models.CharField(max_length=20,choices=client_choices)
    owner = models.CharField("Company Owner", blank=False, max_length=200)
    owner_phone = models.CharField('Owner Phone', max_length=25, blank=False)   
    address = models.CharField(max_length=200)
    zip_code = models.CharField('Zip Code', max_length=15)
    web = models.URLField('Website Address', blank=True)
    manager_name = models.CharField('Manager', max_length=25, blank=False)      
    manager_phone = models.CharField('Manager Phone', max_length=25, blank=False)   
    manager_email = models.EmailField('Manager Email', blank=True) 
    assistant = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name
    
class Vendor(models.Model):
    name = models.CharField('Vendor', max_length=200)
    owner = models.CharField("Company Owner", blank=False, max_length=200)
    owner_phone = models.CharField('Owner Phone', max_length=25, blank=False)   
    address = models.CharField(max_length=200)
    zip_code = models.CharField('Zip Code', max_length=15)
    web = models.URLField('Website Address', blank=True)
    manager_name = models.CharField('Manager', max_length=25, blank=False)      
    manager_phone = models.CharField('Manager Phone', max_length=25, blank=False)   
    manager_email = models.EmailField('Manager Email', blank=True)
    assistant = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField('Product', max_length=200)
    code = models.CharField(max_length=200)
    price = models.IntegerField(blank=False)
    moq = models.IntegerField(blank=False)   
    lead_time = models.DurationField(max_length=200)
    quality_standard = models.CharField('Standard',max_length=200)
    design_size  = models.CharField('width x depth x height', blank=True,max_length=200)
    design_image = models.ImageField(null=True,blank=True, upload_to="images/") 
    design_file = models.FileField(blank=True) 
    material = models.TextField()
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    assistant = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField('Aprroved', default=False)
       
    def __str__(self):
        return self.name
    

class Order(models.Model):
    name = models.CharField('Order Number', max_length=200)
    code_order = models.CharField('Order Code', max_length=200)
    code_shipping = models.CharField('Shipping Code', max_length=200)
    price = models.IntegerField(blank=False)
    lead_time = models.DurationField(max_length=200)
    item_list = models.ManyToManyField(Item,related_name='ordered_item')
    item_price= models.ManyToManyField(Item,related_name='ordered_price')
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    assistant = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

       
    def __str__(self):
        return self.name  
    



