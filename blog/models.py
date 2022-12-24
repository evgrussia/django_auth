from django.db import models
from core.models import User
from django.utils import timezone
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel
)


class Blog(TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel):

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ["id"]

    def __str__(self):
        return self.title

    name = models.CharField(max_length=255, blank=False)
    last_update = models.DateTimeField(default=timezone.now)
    read_time = models.CharField(max_length=255, blank=False)
    text = models.TextField()
    category = models.CharField(max_length=255, blank=False)