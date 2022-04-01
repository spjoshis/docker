"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, cms_view
from products.views import category_view, product_create, product_update

urlpatterns = [
    path('', home_view, name='home'),
    path('product/create', product_create, name='product_create'),
    path('product/<int:id>/', product_update, name='product_update'),
    path('category', category_view, name='categories'),
    path('about', cms_view, name='cms'),
    path('terms', cms_view, name='terms'),
    path('admin/', admin.site.urls),
]
