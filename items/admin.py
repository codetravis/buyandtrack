from django.contrib import admin
from items.models import Item, Category, Location

class ItemAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Category)
