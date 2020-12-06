from django.shortcuts import render
import requests
from .models import Breakfast, Lunch, Dinner

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

    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'
    for product in eating:
        res = requests.get(url.format(product.product_name)).json()
        list_dict = res["foods"][0]["foodNutrients"]

        energy_dict = next(item for item in list_dict if item["nutrientName"] == "Energy")
        protein_dict = next(item for item in list_dict if item["nutrientName"] == "Protein")
        carbohydrate_dict = next(item for item in list_dict if item["nutrientName"] == "Carbohydrate, by difference")
        fat_dict = next(item for item in list_dict if item["nutrientName"] == "Total lipid (fat)")

        product_info = {
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
        list_dict = res["foods"][0]["foodNutrients"]

        energy_dict = next(item for item in list_dict if item["nutrientName"] == "Energy")

        sum+=energy_dict["value"]
    return sum

def create_breakfast(request):
    return render(request, 'counter/create_breakfast.html')

def create_lunch(request):
    return render(request, 'counter/create_lunch.html')

def create_dinner(request):
    return render(request, 'counter/create_dinner.html')
