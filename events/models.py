from django.db import models
from core.models import User
from django.utils import timezone
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel
)


class Events(TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel):

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ["id"]

    def __str__(self):
        return self.title

    category = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    last_update = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=50, blank=False)
    text = models.TextField()

