from django.urls import path, include
from .views import RegisterUserView, LoginAPIView
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path("ap1/v1/register/", RegisterUserView.as_view(), name="register"),
    path("ap1/v1/login/", LoginAPIView.as_view(), name="login"),
]
