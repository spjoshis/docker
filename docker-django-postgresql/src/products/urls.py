from django.urls import path

from products.views import category_view, product_create, product_update

app_name = 'products'
urlpatterns = [
    path('create', product_create, name='product_create'),
    path('<int:id>', product_update, name='product_update'),
    path('list', category_view, name='product_list'),
]
