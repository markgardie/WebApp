from .models import Product
from django.forms import ModelForm, TextInput

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'product',
            'id': 'product',
            'placeholder': 'Продукт'
        })}
