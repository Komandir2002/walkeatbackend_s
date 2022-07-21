from django.urls import path
from .views import RegisterUserView, LoginAPIView

urlpatterns = [
    path("ap1/v1/register/", RegisterUserView.as_view(), name="register"),
    path("ap1/v1/login/", LoginAPIView.as_view(), name="login"),
]
