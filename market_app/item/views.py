from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def details(request, pk):

    item = get_object_or_404(Item, pk = pk)
    # Gets first 3 items in the same category as the 'item' that are not sold, and excludes the item that has the same primary key
    related_items = Item.objects.filter(category = item.category, is_sold = False).exclude(pk = pk)[:3]

    return render(request, "item/detail.html", {

        "item": item,
        "related_items": related_items

    })