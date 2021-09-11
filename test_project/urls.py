from django.contrib import admin
from django.urls import path, include
# from projectapp.ViewSetUrls import routerUrls
# from projectapp.ViewSetUrls import AsViewUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('projectapp.ViewSetUrls.routerUrls')),
    # path('', include('projectapp.ViewSetUrls.AsViewUrls')),
    path('user/', include('accountapp.urls')),
    path('article/', include('articleapp.urls')),
]
