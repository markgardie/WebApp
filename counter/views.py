from django.shortcuts import render
import requests
from .models import Breakfast, Lunch, Dinner

def index(request):

    breakfast = Breakfast.objects.all()
    lunch = Lunch.objects.all()
    dinner = Dinner.objects.all()

    breakfast_info = api(request, breakfast)
    lunch_info = api(request, lunch)
    dinner_info = api(request, dinner)

    context = {
        'breakfast_info': breakfast_info,
        'lunch_info': lunch_info,
        'dinner_info': dinner_info,
    }

    return render(request, 'counter/index.html', context)

def api(request, eating):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'

    eating_info = []

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

        eating_info.append(product_info)

    return eating_info
