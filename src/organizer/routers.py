"""URL Paths and Routers for Organizer App"""
from rest_framework.routers import SimpleRouter

from .viewsets import WodViewSet, TagViewSet
api_router = SimpleRouter()
api_router.register( "wod", WodViewSet, base_name="api-wod" )
api_router.register("tag", TagViewSet, base_name="api-tag")

urlpatterns = api_router.urls