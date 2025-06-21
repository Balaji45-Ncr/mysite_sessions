from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import choices

# Fake product data (like a mini-database)
# PRODUCTS = {
#     101: {"name": "Laptop", "price": 50000},
#     202: {"name": "Phone", "price": 25000},
#     303: {"name": "Headphones", "price": 2000},
# }
# def add_to_cart(request,product_id):
#     if product_id not in PRODUCTS:
#         return HttpResponse('Invalid product ID')
    

def get_or_create(request):
    namess,yes=choices.objects.get_or_create(name='dhoni',defaults={'scores':98})
    print(namess)
    return HttpResponse(f"dhoni score is {namess.name}")
 