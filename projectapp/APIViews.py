from .models import Blog
from .serializers import BlogSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Blog 목록을 보여주는 역할 (2가지 HTTP method가 필요)
class BlogList(APIView):
  # list
  def get(self, request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

  # create
  def post(self, request):
    # request.data는 사용자의 입력 데이터
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

blog_list = BlogList.as_view()


# Blog의 detail (3가지 HTTP method가 필요)
class BlogDetail(APIView):
  # Blog 단일 객체 가져오기
  def get_object(self, pk):
    try:
      return Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
      raise Http404

  # Blog의 detail 보기
  def get(self, request, pk, format=None):
    blog = self.get_object(pk)  # 상단에 get_object 를 가져온다
    serializer = BlogSerializer(blog)
    return Response(serializer.data)  # 단일객체를 json 으로 Response 한다

  # Blog 수정
  def put(self, request, pk, format=None):
    blog = self.get_object(pk)
    serializer = BlogSerializer(blog, data=request.data)  # 단일객체(=인스턴스)와 입력값을 인자로 지정
    if serializer.is_valid():  # is_valid() 는 create 와 put 에만 있다.
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # Blog 삭제하기
  def delete(self, request, pk, format=None):
    blog = self.get_object(pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

blog_detail = BlogDetail.as_view()