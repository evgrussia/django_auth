from .serializers import BlogSerializer
from .models import Blog
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin


class BlogViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        viewsets.GenericViewSet
        ):
    """
    A simple ViewSet for listing or retrieving items.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
