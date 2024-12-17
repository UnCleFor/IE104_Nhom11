from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrangChu, name='TrangChu'),
    path('Truyền thông/', views.TruyenThong, name='TruyenThong'),
     path('Tìm kiếm/', views.TimKiem, name='TimKiem'),
    
    path('Đăng nhập/', views.DangNhap, name='DangNhap'),
    path('Đăng ký/', views.DangKy, name='DangKy'),
    path('Đăng xuất/', views.DangXuat, name='DangXuat'),
    path('Giỏ hàng/', views.GioHang, name='GioHang'),
    path('Đặt hàng/', views.DatHang, name='DatHang'),
    
    path('update_item/', views.updateItem, name='update_item'),
    
    
    path('Trang cá nhân/', views.TrangCaNhan, name='TrangCaNhan'),
    path('Edit trang cá nhân/', views.EditTrangCaNhan, name='EditTrangCaNhan'),
    
    
    path('Đơn hàng của tôi/', views.DonHangCuaToi, name='DonHangCuaToi'),
    # path('Chi tiết đơn hàng', views.ChiTietDonHang, name='ChiTietDonHang'),
    
    path('Giới thiệu/', views.GioiThieu, name='GioiThieu'),
    path('Quy chế hoạt động/', views.QuyCheHoatDong, name='QuyCheHoatDong'),
    path('Chính sách nội dung/', views.ChinhSachNoiDung, name='ChinhSachNoiDung'),
    path('Chính sách đổi trả/', views.ChinhSachDoiTra, name='ChinhSachDoiTra'),
    path('Chính sách thanh toán/', views.ChinhSachThanhToan, name='ChinhSachThanhToan'),

    
    path('<str:cate_lv1_name>/', views.PList_Lv1, name='categories_products'),
    path('<str:cate_lv1_name>/<str:cate_lv2_name>/', views.PList_Lv2, name='categories_lv2'),
    path('<str:cate_lv1_name>/<str:cate_lv2_name>/<str:product_name>/', views.ChiTietSanPham, name='product_detail'),
]

   
   
# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)