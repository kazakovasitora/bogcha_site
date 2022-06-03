from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('senuchunadminman/', admin.site.urls),
    path('', include('bogcha_ilova.urls')),
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)