from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from . import GenericsViews

urlpatterns =[
    path('blog/', GenericsViews.BlogList.as_view()),
    path('blog/<int:pk>/', GenericsViews.BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
