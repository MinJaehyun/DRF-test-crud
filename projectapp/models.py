from django.db import models


class Blog(models.Model):  # 게시판 기능
    title       = models.CharField(max_length=100)
    description = models.TextField()
