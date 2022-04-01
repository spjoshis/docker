from django.shortcuts import render, get_object_or_404
from .models import Product

from .forms.product_create import ProductCreateForm, ProductCreateRawForm

def product_create(request):
    form = ProductCreateForm(request.POST or None)
    params = {'msg': ''}

    # Validation
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
        params['msg'] = "Product added successfully"

    params['form'] = form
    return render(request, 'products/create.html', params)

def product_update(request, id):
    # Get products
    product = get_object_or_404(Product, id=id)
    form = ProductCreateForm(request.POST or None, instance=product)
    params = {'msg': ''}

    # Validation
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
        params['msg'] = "Product updated successfully"

    params['form'] = form
    return render(request, 'products/update.html', params)


def category_view(request, *args, **kwargs):

    # Get products
    products = Product.objects.all()
    params = {
        'name': 'Products',
        'products': products
    }
    return render(request, 'products/category.html', params)