from django.contrib import admin
from . import models
from .forms import *
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    form = ItemAdminForm


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item')


admin.site.register(Item, ItemAdmin, )
admin.site.register(Order, OrderAdmin,)
