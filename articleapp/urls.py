from django.urls import path, include
from rest_framework.routers import DefaultRouter

from articleapp.views import ArticleViewSet

router = DefaultRouter()
router.register('', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
