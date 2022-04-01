from django import forms
from django.db import models

from products.models import Product

class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=120, label="Product Title")  # max_length = required
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class",
        "rows": 5,
        "cols": 21
    }))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if 'Gopal' in title:
            raise forms.ValidationError("Please write correct title")
        else:
            return title


    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get("description")
        if 'Gopal' in description:
            raise forms.ValidationError("Please write correct description")
        else:
            return description

class ProductCreateRawForm(forms.Form):
    title = forms.CharField(max_length=120, label="Product Title")  # max_length = required
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class",
        "rows": 5,
        "cols": 21
    }))
    price = forms.DecimalField(initial=199.99)
