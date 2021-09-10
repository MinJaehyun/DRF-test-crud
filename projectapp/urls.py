from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('blog/', views.blog_list),
    path('blog/<int:pk>/', views.blog_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# 필수는 아니지만 format_suffix_patterns 으로 특정 포맷을 간단, 명확하게 참조할 수 있다