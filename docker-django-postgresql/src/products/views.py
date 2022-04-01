from django.shortcuts import render
from .models import Product

# Create your views here.

def category_view(request, *args, **kwargs):

    # Get products
    products = Product.objects.all()
    params = {
        'name': 'Products',
        'products': products
    }
    return render(request, 'products/category.html', params)