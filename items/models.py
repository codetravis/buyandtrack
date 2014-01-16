from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    month = models.IntegerField()
    day = models.IntegerField()
    year = models.IntegerField()
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name
    
# Quick and Dirty Totals through receipts
class Receipt(models.Model):
    month = models.IntegerField()
    day = models.IntegerField()
    year = models.IntegerField()
    total = models.DecimalField(decimal_places=2, max_digits=9)

    def __unicode__(self):
        return "%d/%d/%d -- %s" % (self.month, self.day, self.year, str(self.total))

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt

# Form classes for input
class ItemForm(ModelForm):
    class Meta:
        model = Item

class CategoryForm(ModelForm):
    class Meta:
        model = Category

class LocationForm(ModelForm):
    class Meta:
        model = Location
