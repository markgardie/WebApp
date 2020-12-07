from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('library', views.library, name='library'),
    path('library/create_product', views.ProductCreateView.as_view(), name = "create_product"),
    path('library/<int:pk>/delete_product', views.ProductDeleteView.as_view(), name='delete_product'),
]
