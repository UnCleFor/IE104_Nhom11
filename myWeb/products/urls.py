from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.PList_ThucPhamChucNang, name='PList_ThucPhamChucNang'),
]
# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)