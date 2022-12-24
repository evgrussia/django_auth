from django.contrib import admin
from . import models
from .forms import *
from .models import *


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    form = EventsAdminForm


admin.site.register(Events, EventsAdmin, )