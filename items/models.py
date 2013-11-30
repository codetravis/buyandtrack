from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class ItemType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    item_type = models.ForeignKey(ItemType)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    purchase_date = models.DateField('purchase date')
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name
    

# Form classes for input
class ItemForm(ModelForm):
    class Meta:
        model = Item

class ItemTypeForm(ModelForm):
    class Meta:
        model = ItemType

class LocationForm(ModelForm):
    class Meta:
        model = Location
