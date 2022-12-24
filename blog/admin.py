from django.contrib import admin
from . import models
from .forms import *
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    form = BlogAdminForm


admin.site.register(Blog, BlogAdmin, )