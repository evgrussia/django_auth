from .models import Events
from rest_framework_json_api import serializers


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = (
            'title',
            'category',
            'name',
            'description',
            'last_update',
            'time',
            'text'
        )