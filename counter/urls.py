
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "counter_index"),
    path('/create_breakfast', views.BreakfastCreate.as_view(), name = "create_breakfast"),
    path('/create_lunch', views.LunchCreate.as_view(), name = "create_lunch"),
    path('/create_dinner', views.DinnerCreate.as_view(), name = "create_dinner"),
]
