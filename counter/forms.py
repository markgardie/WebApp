from .models import Breakfast, Lunch, Dinner
from django.forms import ModelForm, TextInput

class BreakfastForm(ModelForm):
    class Meta:
        model = Breakfast
        fields = ['product_name']

class LunchForm(ModelForm):
    class Meta:
        model = Breakfast
        fields = ['product_name']

class DinnerForm(ModelForm):
    class Meta:
        model = Breakfast
        fields = ['product_name']
