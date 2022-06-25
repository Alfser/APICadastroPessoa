from rest_framework import routers

from .views import PersonViewSet

route = routers.DefaultRouter()

route.register('pessoas', PersonViewSet, basename='people')
