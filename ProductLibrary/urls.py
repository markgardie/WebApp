from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('library', views.create, name='library'),
    path('signin', views.sign, name='signin'),
]
