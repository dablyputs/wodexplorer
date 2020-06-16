"""Viewsets for the Organizer App"""
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.viewsets import ModelViewSet

from .models import Wod
from .serializers import WodSerializer

class WodViewSet(ModelViewSet):
    """A set of views for the Startup model"""
    lookup_field = "pk"
    queryset = Wod.objects.all()
    serializer_class = WodSerializer