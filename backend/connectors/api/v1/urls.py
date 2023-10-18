from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import proxtestconnectViewSet

router = DefaultRouter()
router.register("proxtestconnect", proxtestconnectViewSet, basename="proxtestconnect")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
