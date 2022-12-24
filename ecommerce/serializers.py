from .models import Item, Order
from rest_framework_json_api import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = (
            'title',
            'name',
            'description',
            'price',
            'bv_balls',
        )


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=False)

    class Meta:
        model = Order
        fields = (
            'item',
            'data',
            'amount',
            'payment_gateway',
            'order_status',
        )
