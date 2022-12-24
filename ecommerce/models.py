from django.db import models
from core.models import User
from django.utils import timezone
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel
)


class Item(TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel):

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ["id"]

    def __str__(self):
        return self.title

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    price = models.FloatField(max_length=255, blank=False, default=0.00)
    bv_balls = models.FloatField(max_length=255, blank=False, default=0.00)

    def place_order(self, user):
        # used to place an order
        return Order.objects.create(item=self, user=user)


class Order(TimeStampedModel, ActivatorModel):

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ["id"]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
    amount = models.FloatField(max_length=255, blank=False, default=0.00)
    payment_gateway = models.CharField(max_length=255, blank=False)
    order_status = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.user.username} - {self.item.title}'
