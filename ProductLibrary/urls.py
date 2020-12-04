from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),

    path('library', views.library, name='library'),

    path('signin', views.signin, name='signin'),
]
