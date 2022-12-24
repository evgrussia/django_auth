from .serializers import EventsSerializer
from .models import Events
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin


class EventsViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        viewsets.GenericViewSet
        ):
    """
    A simple ViewSet for listing or retrieving items.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
