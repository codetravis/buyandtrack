from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from items.models import Item, Location, ItemType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from items.analyze_items import LowestPriceItem
 
def index(request):
    context = {}
    # create list of last 7 purchased items
    purchased_items = Item.objects.order_by('-purchase_date')[:7]
    context = {'purchased_items': purchased_items}
    return render(request, 'items/index.html', context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'items/detail.html', {'item': item})


def item_type_detail(request, item_type_id):
    # get averages from last 10 
    item_type = get_object_or_404(ItemType, pk=item_type_id)
    best_price_item = LowestPriceItem(item_type_id, 10)
    
    return render(request, 'items/item_type_detail.html', 
        {'best_price_item': best_price_item, 'item_type': item_type})

def add_item(request):
    """
    Add new item to listing.
    """    
    return render(request, 'items/add_item.html', {})
