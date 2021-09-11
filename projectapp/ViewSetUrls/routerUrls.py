from django.urls import path, include
from projectapp.ViewSetViews import BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog', BlogViewSet)
# 첫 번째 인자: url의 prefix , # 두 번째 인자: ViewSet

urlpatterns =[
    path('', include(router.urls))
]