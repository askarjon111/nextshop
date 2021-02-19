from django.shortcuts import render
from .models import *

def index(request):
    products = Product.objects.order_by('-product_date').filter(in_stock=True)

    context = {
        'products' : products
    }

    return render(request, 'shop/index.html', context)

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product': product
    }

    return render(request, '../templates/shop/product_detail.html', context)
