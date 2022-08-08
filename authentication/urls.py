from django.urls import path, include
from .views import UserViewSet, LoginAPIView
from rest_framework.routers import DefaultRouter
ROUTER = DefaultRouter()
ROUTER.register(r"account", UserViewSet)

urlpatterns = [
    path("api/v1/", include(ROUTER.urls)),
    path("api/v1/login/", LoginAPIView.as_view(), name="login"),
]
