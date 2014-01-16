from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from items.models import Item, Location, Category, Receipt
from items.models import ItemForm, CategoryForm, LocationForm, ReceiptForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from items.analyze_items import LowestPriceItem
 
def index(request):
    
    context = {}
    # create list of last 7 purchased items
    purchased_items = Item.objects.filter(year=2014)[:20]
    context = {'purchased_items': purchased_items}
    return render(request, 'items/index.html', context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'items/detail.html', {'item': item})


def category_detail(request, category_id):
    # get averages from last 10 
    category = get_object_or_404(Category, pk=category_id)
    items_in_category = Items.objects.filter(category=category)[:10]
    return render(request, 'items/category_detail.html', 
        {'items_in_category': items_in_category, 'category': category})

def add_item(request):
    """
    Add new item to listing.
    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/items/')
    else:
        form = ItemForm()    
    return render(request, 'items/add_item.html', {'form': form})

def add_receipt(request):
    """
    Add new receipt to listing
    """
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/items/')
    else:
        form = ReceiptForm()
    return render(request, 'items/add_receipt.html', {'form': form})

def add_category(request):
    """
    Add new item type to listing.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/items/')
    else:
        form = CategoryForm()
    return render(request, 'items/add_category.html', {'form': form})

def add_location(request):
    """
    Add new location to listing.
    """
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/items/')
    else:
        form = LocationForm()
    return render(request, 'items/add_location.html', {'form': form})

def monthly_report(request, year, month):
    """
    Show the Monthly breakdown of the spending
    """
    report_year = year
    report_month = month
    context = {'year': report_year, 'month': report_month}
    expenses = Item.objects.filter(year=report_year).filter(month=report_month)
    total = 0
    for item in expenses:
        total += item.price * item.quantity
    context['total'] = total

    receipts = Receipt.objects.filter(year=report_year).filter(month=report_month)
    receipt_total = 0
    for rcpt in receipts:
        receipt_total += rcpt.total
    context['receipt_total'] = receipt_total
    return render(request, 'items/monthly_report.html', context)


