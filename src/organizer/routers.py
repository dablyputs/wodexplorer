"""URL Paths and Routers for Organizer App"""
from rest_framework.routers import SimpleRouter

from .viewsets import WodViewSet
api_router = SimpleRouter()
api_router.register( "wod", WodViewSet, base_name="api-wod" )

urlpatterns = api_router.urls