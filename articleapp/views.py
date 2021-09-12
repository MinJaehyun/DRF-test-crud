from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Article
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer


# Blog의 list, create, retrieve, update, destroy
class ArticleViewSet(viewsets.ModelViewSet):
  authentication_classes = [BasicAuthentication, SessionAuthentication]    # authentication 추가
  permission_classes     = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # permission 추가
  queryset               = Article.objects.all()
  serializer_class       = ArticleSerializer

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
