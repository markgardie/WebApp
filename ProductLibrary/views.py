import requests
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .forms import ProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    return render (request, 'ProductLibrary/index.html')

def library(request):
    product = Product.objects.all()

    all_info = products_info(request, product)

    context = {
        'all_info': all_info
    }

    return render(request, 'ProductLibrary/library.html', context)

def products_info(request,  products):
    prod_info = []
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=zbfgBNQzv1ZfcoGcl4ekXGhGikM6C8otSs5siNpl&query={}&pageSize=1'
    error = 'Такого продукта нет. Вводите продукт на английском'

    for product in products:
        res = requests.get(url.format(product.name)).json()

        if not res["foods"]:
            product_info = {
                'id': product.id,
                'name': product.name,
                'error': error
            }

            prod_info.append(product_info)
        else:
            list_dict = res["foods"][0]["foodNutrients"]

            energy_dict = next(item for item in list_dict if item["nutrientName"] == "Energy")
            protein_dict = next(item for item in list_dict if item["nutrientName"] == "Protein")
            carbohydrate_dict = next(item for item in list_dict if item["nutrientName"] == "Carbohydrate, by difference")
            fat_dict = next(item for item in list_dict if item["nutrientName"] == "Total lipid (fat)")

            product_info = {
                'id': product.id,
                'name': product.name,
                'energy': energy_dict["value"],
                'protein': protein_dict["value"],
                'carbohydrate':carbohydrate_dict["value"],
                'fat': fat_dict["value"],
            }

            prod_info.append(product_info)

    return prod_info


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('library')

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('library')
