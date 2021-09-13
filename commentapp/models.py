from django.db import models


class Comment(models.Model):
    blog       = models.ForeignKey('articleapp.Article', null=False, blank=False, on_delete=models.CASCADE)
    author     = models.ForeignKey('accountapp.User', null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    comment    = models.TextField()

    def __str__(self):
        return self.comment
