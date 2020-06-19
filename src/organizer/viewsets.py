"""Viewsets for the Organizer App"""
from rest_framework.viewsets import ModelViewSet

from .models import Wod, Tag
from .serializers import WodSerializer, TagSerializer

class WodViewSet(ModelViewSet):
    """A set of views for the Wod model"""
    lookup_field = "pk"
    queryset = Wod.objects.all()
    serializer_class = WodSerializer

class TagViewSet(ModelViewSet):
    """A set of views for the Tag model"""

    lookup_field = "slug"
    queryset = Tag.objects.all()
    serializer_class = TagSerializer