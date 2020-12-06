
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name = "counter_index"),

    path('/create_breakfast', views.BreakfastCreate.as_view(), name = "create_breakfast"),
    path('/create_lunch', views.LunchCreate.as_view(), name = "create_lunch"),
    path('/create_dinner', views.DinnerCreate.as_view(), name = "create_dinner"),

    path('/<int:pk>/delete_breakfast', views.BreakfastDelete.as_view(), name = "delete_breakfast"),
    path('/<int:pk>/delete_lunch', views.LunchDelete.as_view(), name = "delete_lunch"),
    path('/<int:pk>/delete_dinner', views.DinnerDelete.as_view(), name = "delete_dinner"),
]
