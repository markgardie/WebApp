from django.shortcuts import render
import requests
from .models import Breakfast, Lunch, Dinner

def index(request):

    context = {
        'breakfast_info': breakfast_render(request),
        'lunch_info': lunch_render(request),
        'dinner_info': dinner_render(request),
    }

    return render(request, 'counter/index.html', context)

def breakfast_render(request):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'

    breakfast_info = []
    breakfast = Breakfast.objects.all()

    for product in breakfast:
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

        breakfast_info.append(product_info)

    return breakfast_info

def lunch_render(request):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'

    lunch_info = []
    lunch = Lunch.objects.all()

    for product in lunch:
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

        lunch_info.append(product_info)

    return lunch_info

def dinner_render(request):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'

    dinner_info = []
    dinner = Dinner.objects.all()

    for product in dinner:
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

        dinner_info.append(product_info)

    return dinner_info
