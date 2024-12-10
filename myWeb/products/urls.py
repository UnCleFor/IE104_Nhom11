from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrangChu, name='TrangChu'),
    path('Truyền thông/', views.TruyenThong, name='TruyenThong'),
    path('<str:cate_lv1_name>/', views.PList_Lv1, name='categories_products'),
    path('<str:cate_lv1_name>/<str:cate_lv2_name>/', views.PList_Lv2, name='categories_lv2'),
   
]

   
   
# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)