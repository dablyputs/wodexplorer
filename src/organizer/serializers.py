"""Serializers for the Organizer App

Serializer Documentation
http://www.django-rest-framework.org/api-guide/serializers/
http://www.django-rest-framework.org/api-guide/fields/
http://www.django-rest-framework.org/api-guide/relations/
"""
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import Wod


class WodSerializer(HyperlinkedModelSerializer):
    """Serialize Wod data"""

    class Meta:
        model = Wod
        fields = "__all__"
