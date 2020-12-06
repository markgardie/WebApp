from django.shortcuts import render, redirect
import requests
from django.urls import reverse_lazy

def login(request):
    return render(request, 'accounts/login.html')
