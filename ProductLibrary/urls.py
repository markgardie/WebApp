from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('library', views.create, name='library'),
    path('signin', views.sign, name='signin'),
]
