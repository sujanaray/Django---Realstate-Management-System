from django.db import models

from datetime import datetime

# Create your models here.
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor , on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2 , decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5 , decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now , blank=True)

    def __str__(self):
        return self.title
#The __str__() method is called whenever you call str() on an object. Django uses str(obj) in a number of places. Most notably, to display an object in the Django admin site and as the value inserted into a template when it displays an object. Thus, you should always return a nice, human-readable representation of the model from the __str__() method.





 
