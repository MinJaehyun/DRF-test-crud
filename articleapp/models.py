from django.db import models

from test_project import settings


class Article(models.Model):
  # User 와 Article 의 관계: 1:N
  author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # null=True, blank=Tue 지정 하지 않음.
  title      = models.CharField(max_length=100)
  content    = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)



