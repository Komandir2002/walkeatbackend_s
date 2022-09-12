from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import swagger

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('',include('menu_api.urls'))
] + swagger.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
