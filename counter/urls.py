
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "counter_index"),
    path('/create_breakfast', views.create_breakfast, name = "create_breakfast"),
    path('/create_lunch', views.create_lunch, name = "create_lunch"),
    path('/create_dinner', views.create_dinner, name = "create_dinner"),
]
