from django.contrib import admin
from django.urls import path, include
from projectapp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projectapp.urls')),
]