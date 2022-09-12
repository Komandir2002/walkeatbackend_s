from django.urls import path, include
from .views import LoginAPIView, RegisterView, VerifyEmail, ProfileViewSet, CardViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)


ROUTER = DefaultRouter()
ROUTERCARD = DefaultRouter()
ROUTER.register(r"profile", ProfileViewSet, "profile_api")
ROUTERCARD.register(r"card", CardViewSet, "card_api")


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify"),
    path("", include(ROUTER.urls)),
    path("", include(ROUTERCARD.urls)),
    path("api/token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
]
