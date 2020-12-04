import requests
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .forms import ProductForm


def index(request):
    return render (request, 'index.html')


def create(request):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'

    if(request.method == 'POST'):
        form = ProductForm(request.POST)
        form.save()

    form = ProductForm()

    products = Product.objects.all()

    all_products = []

    for product in products:
        res = requests.get(url.format(product.name)).json()
        list_dict = res["foods"][0]["foodNutrients"]


        energy_dict = next(item for item in list_dict if item["nutrientName"] == "Energy")
        protein_dict = next(item for item in list_dict if item["nutrientName"] == "Protein")
        carbohydrate_dict = next(item for item in list_dict if item["nutrientName"] == "Carbohydrate, by difference")
        fat_dict = next(item for item in list_dict if item["nutrientName"] == "Total lipid (fat)")

        product_info = {
            'name': product.name,
            'energy': energy_dict["value"],
            'protein': protein_dict["value"],
            'carbohydrate':carbohydrate_dict["value"],
            'fat': fat_dict["value"],
        }

        all_products.append(product_info)

    context = {'all_info': all_products, 'form': form}

    return render(request, 'library.html', context)

def sign(request):
        return render(request, 'signin.html')
