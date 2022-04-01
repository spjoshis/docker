from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Product

from .forms.product_create import ProductCreateForm, ProductCreateRawForm

def product_create(request):
    form = ProductCreateForm(request.POST or None)
    params = {}

    # Validation
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/product/list')

    params['form'] = form
    return render(request, 'products/create.html', params)

def product_update(request, id):
    # Get products
    product = get_object_or_404(Product, id=id)
    form = ProductCreateForm(request.POST or None, instance=product)
    params = {}
    # Validation
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/product/list')

    params['form'] = form
    return render(request, 'products/update.html', params)


def category_view(request, *args, **kwargs):
    url = reverse('products:product_create', kwargs={})

    # Get products
    products = Product.objects.order_by('id').all()
    params = {
        'name': 'Products',
        'products': products,
        'url': url
    }
    return render(request, 'products/category.html', params)