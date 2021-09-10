from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework import mixins


# Blog list 보여준다
class BlogList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer

  # Blog list
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  # Blog create
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


# Blog의 detail 보여준다
class BlogDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer

  # Blog detail
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  # Blog retrieve
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  # Blog delete
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
