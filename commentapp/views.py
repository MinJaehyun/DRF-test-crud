from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from articleapp.permissions import IsOwnerOrReadOnly
from commentapp.models import Comment
from commentapp.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
  authentication_classes = [BasicAuthentication, SessionAuthentication]
  permission_classes     = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  queryset               = Comment.objects.all()
  serializer_class       = CommentSerializer

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
