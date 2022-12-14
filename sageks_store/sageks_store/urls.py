from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('catalog/', include('catalog.urls')),
    path('basket/', include('basket.urls')),
    path('order/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
