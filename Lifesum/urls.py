
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProductLibrary.urls')),
    path('counter', include('counter.urls')),
]
