from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(default="Basic description")
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product_update', kwargs={'id': self.id})