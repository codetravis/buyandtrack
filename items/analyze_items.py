

from items.models import Item, Category, Location


def CheckNumItems(num_items):
    if num_items > 100:
        return 100
    elif num_items < 1:
        return 1
    else:
        return num_items
    

def LowestPriceItem(category_id, num_items):
    """ 
    Given an item_type_id, returns the item with best price per quantity.
    Never looks at more than 100 items
    """
    num_items = CheckNumItems(num_items)
    best_item = {'name': -1, 'price': -1, 'location': -1}
    item_list = Item.objects.all().filter(category=category_id)[:num_items]
    if len(item_list) > 0:
        best_item['price'] = item_list[0].price/item_list[0].quantity
        best_item['name'] = item_list[0].name
        best_item['location'] = item_list[0].location
        for item in item_list:
            new_price =  (item.price/item.quantity) 
            if new_price < best_item['price']:
                best_item['price'] = new_price
                best_item['name'] = item.name
                best_item['location'] = Location.objects.get(pk=item.location)
    return best_item


def AveragePrice(category_id, num_items):
    """
    Given an item_type_id and number of items, returns the average purchase
    price of the items.
    """
    num_items = CheckNumItems(num_items)

    return 0
