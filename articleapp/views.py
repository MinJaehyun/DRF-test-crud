from rest_framework.viewsets import ModelViewSet

from articleapp.models import Article
from articleapp.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
  queryset         = Article.objects.all()
  serializer_class = ArticleSerializer
