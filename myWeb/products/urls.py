from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.PList_ThucPhamChucNang, name='PList_ThucPhamChucNang'),
]