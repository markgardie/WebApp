from django.shortcuts import render, redirect
import requests
from .models import Breakfast, Lunch, Dinner
from .forms import BreakfastForm, LunchForm, DinnerForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):

    breakfast = Breakfast.objects.all()
    lunch = Lunch.objects.all()
    dinner = Dinner.objects.all()

    breakfast_info = eating_info(request, breakfast)
    lunch_info = eating_info(request, lunch)
    dinner_info = eating_info(request, dinner)

    context = {
        'breakfast_info': breakfast_info,
        'lunch_info': lunch_info,
        'dinner_info': dinner_info,
        'calorie': counter(request, breakfast, lunch, dinner),
    }

    return render(request, 'counter/index.html', context)

def eating_info(request, eating):
    eat_info = []
    error = 'Такого продукта нет. Вводите продукт на английском'


    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'
    for product in eating:
        res = requests.get(url.format(product.product_name)).json()
        if not res["foods"]:
            product_info = {
                'id': product.id,
                'name': product.product_name,
                'error': error
            }
            eat_info.append(product_info)
        else:

            list_dict = res["foods"][0]["foodNutrients"]

            energy_dict = next(item for item in list_dict if item["nutrientName"] == "Energy")
            protein_dict = next(item for item in list_dict if item["nutrientName"] == "Protein")
            carbohydrate_dict = next(item for item in list_dict if item["nutrientName"] == "Carbohydrate, by difference")
            fat_dict = next(item for item in list_dict if item["nutrientName"] == "Total lipid (fat)")

            product_info = {
                'id': product.id,
                'name': product.product_name,
                'energy': energy_dict["value"],
                'protein': protein_dict["value"],
                'carbohydrate':carbohydrate_dict["value"],
                'fat': fat_dict["value"],
            }

            eat_info.append(product_info)

    return eat_info

def counter(request, breakfast, lunch, dinner):
    sum = loop(request, breakfast) + loop(request, lunch) + loop(request, dinner)
    return sum

def loop(request, eating):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'
    sum = 0

    for product in eating:
        res = requests.get(url.format(product.product_name)).json()

        if not res["foods"]:
            sum+=0
        else:
            list_dict = res["foods"][0]["foodNutrients"]
            energy_dict = next(item for item in list_dict if item["nutrientName"] == "Energy")
            sum+=energy_dict["value"]
    return sum

class BreakfastCreate(CreateView):
    model = Breakfast
    fields = '__all__'
    success_url = reverse_lazy('counter_index')

class LunchCreate(CreateView):
    model = Lunch
    fields = '__all__'
    success_url = reverse_lazy('counter_index')

class DinnerCreate(CreateView):
    model = Dinner
    fields = '__all__'
    success_url = reverse_lazy('counter_index')

class BreakfastDelete(DeleteView):
    model = Breakfast
    context_object_name = 'breakfast'
    success_url = reverse_lazy('counter_index')

class LunchDelete(DeleteView):
    model = Lunch
    context_object_name = 'lunch'
    success_url = reverse_lazy('counter_index')

class DinnerDelete(DeleteView):
    model = Dinner
    context_object_name = 'dinner'
    success_url = reverse_lazy('counter_index')
