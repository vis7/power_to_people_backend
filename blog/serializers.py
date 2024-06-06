from django.utils import timezone
from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'likes', 'created_at', 'modified_at', 'created_by', )
        read_only_fields = ['created_by']

    def validate(self, data):
        user = self.context.get('user')
        data['created_by'] = user
        return data

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.modified_at = timezone.now()
        return instance
