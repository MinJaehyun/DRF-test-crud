from rest_framework import serializers

from commentapp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source='user.nickname')

  class Meta:
    model = Comment
    fields = ['id', 'blog', 'user', 'created_at', 'comment']
