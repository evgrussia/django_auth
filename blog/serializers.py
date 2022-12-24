from .models import Blog
from rest_framework_json_api import serializers


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'title',
            'read_time',
            'text',
            'category',
        )