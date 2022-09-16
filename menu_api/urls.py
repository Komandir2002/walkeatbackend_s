from django.urls import path, include
from .views import (
    FitViewSet,
    FitMenuView,
    CategoryView,
    FitListApiView,
    CartViewSet,
    OrderViewSet,
)
from rest_framework.routers import SimpleRouter

ROUTER = SimpleRouter()
ROUTER.register(r"fit-crud", FitViewSet)
ROUTER.register(r"cart", CartViewSet)
ROUTER.register(r"order", OrderViewSet)

urlpatterns = [
    path("", include(ROUTER.urls), name="menu_api"),
    path("menu/", FitMenuView.as_view(), name="main_menu_api"),
    path("categories/", CategoryView.as_view(), name="categories_api"),
    path("menu-detail/", FitListApiView.as_view(), name="detail_fit_api"),
]
