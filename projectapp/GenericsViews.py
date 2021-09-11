from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics


# BlogList - get(list), post(create)
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# BlogDetail - get(retrieve), put(update), delete(destroy)
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer