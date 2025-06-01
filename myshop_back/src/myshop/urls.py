from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("", include("shop.urls", namespace="shop"))]

# admin
urlpatterns += [
    path("admin/", admin.site.urls),
]

# Только для локальной разработки (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
