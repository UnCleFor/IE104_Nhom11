from django.shortcuts import redirect, render, get_object_or_404
from .models import Category_lv1, Category_lv2
from django.core.paginator import Paginator


from .models import Product, Category_lv1, Category_lv2

from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import *
from django.shortcuts import get_object_or_404

def PList_Lv1(request, cate_lv1_name):
    # Lấy danh mục cấp 1 dựa trên tên
    cate_lv1 = get_object_or_404(Category_lv1, cate_1=cate_lv1_name)

    # Lấy danh sách các danh mục cấp 2 thuộc danh mục cấp 1
    categories_lv2 = Category_lv2.objects.filter(cate_1=cate_lv1)

    # Lấy sản phẩm thuộc danh mục cấp 2
    products = Product.objects.filter(prod_cate_lv2__in=categories_lv2)

    # Đếm số lượng sản phẩm của từng category_lv2
    for cate_lv2 in categories_lv2:
        cate_lv2.num_products = Product.objects.filter(prod_cate_lv2=cate_lv2).count()

    # Lấy sản phẩm và gắn URL của ảnh avatar vào từng sản phẩm
    for product in products:
        avatar = Product_Image.objects.filter(prod_name=product, is_avatar=True).first()
        product.avatar_url = avatar.ImageURL if avatar else None

        # Định dạng giá
        product.prod_price_formatted = "{:,.0f}".format(product.prod_price)  # xxx.xxx

        # Định dạng số đã bán và số lượng đánh giá
        if product.prod_sold > 999:
            product.prod_sold_formatted = "{:.1f}k".format(product.prod_sold / 1000)  # 5.1k
        else:
            product.prod_sold_formatted = product.prod_sold

        if product.prod_num_rating > 999:
            product.prod_num_rating_formatted = "{:.1f}k".format(product.prod_num_rating / 1000)  # 5.1k
        else:
            product.prod_num_rating_formatted = product.prod_num_rating

        # Định dạng giá giảm
        if product.prod_discount > 0:
            product.prod_discount_formatted = "{:,.0f} đ".format(product.prod_discount)  # xxx.xxx
        else:
            product.prod_discount_formatted = ''

    # Cập nhật breadcrumb
    breadcrumb = [
        {"name": "Trang chủ", "url": "/"},
        {"name": cate_lv1.cate_1, "url": f"/{cate_lv1.cate_1}/"}
    ]


    # Phân trang với 12 sản phẩm mỗi trang
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Xử lý hiển thị phân trang rút gọn
    total_pages = paginator.num_pages
    current_page = page_obj.number
    if total_pages <= 7:
        page_range = paginator.page_range
    else:
        if current_page <= 4:
            page_range = list(range(1, 6)) + ['...'] + [total_pages]
        elif current_page > total_pages - 4:
            page_range = [1] + ['...'] + list(range(total_pages - 4, total_pages + 1))
        else:
            page_range = (
                [1] + ['...']
                + list(range(current_page - 1, current_page + 2))
                + ['...']
                + [total_pages]
            )

    # Cập nhật context
    context = {
        'cate_lv1': cate_lv1,
        'categories_lv2': categories_lv2,
        'page_obj': page_obj,
        'page_range': page_range,
        'breadcrumb': breadcrumb
    }

    return render(request, 'PList_Lv1.html', context)


def PList_Lv2(request, cate_lv1_name, cate_lv2_name):
    # Lấy danh mục cấp 1 và cấp 2 dựa trên tên
    cate_lv1 = get_object_or_404(Category_lv1, cate_1=cate_lv1_name)
    cate_lv2 = get_object_or_404(Category_lv2, cate_2=cate_lv2_name, cate_1=cate_lv1)

    # Lấy sản phẩm thuộc danh mục cấp 2
    products = Product.objects.filter(prod_cate_lv2=cate_lv2)

    # Lấy sản phẩm và gắn URL của ảnh avatar vào từng sản phẩm
    for product in products:
        avatar = Product_Image.objects.filter(prod_name=product, is_avatar=True).first()
        product.avatar_url = avatar.ImageURL if avatar else None

        # Định dạng giá
        product.prod_price_formatted = "{:,.0f}".format(product.prod_price)

        # Định dạng số đã bán và số lượng đánh giá
        if product.prod_sold > 999:
            product.prod_sold_formatted = "{:.1f}k".format(product.prod_sold / 1000)
        else:
            product.prod_sold_formatted = product.prod_sold

        if product.prod_num_rating > 999:
            product.prod_num_rating_formatted = "{:.1f}k".format(product.prod_num_rating / 1000)
        else:
            product.prod_num_rating_formatted = product.prod_num_rating

        # Định dạng giá giảm
        if product.prod_discount > 0:
            product.prod_discount_formatted = "{:,.0f} đ".format(product.prod_discount)
        else:
            product.prod_discount_formatted = ''

    # Cập nhật breadcrumb
    breadcrumb = [
        {"name": "Trang chủ", "url": "/"},
        {"name": cate_lv1.cate_1, "url": f"/{cate_lv1.cate_1}/"},
        {"name": cate_lv2.cate_2, "url": f"/{cate_lv1.cate_1}/{cate_lv2.cate_2}/"}
    ]


    # Phân trang với 12 sản phẩm mỗi trang
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Xử lý hiển thị phân trang rút gọn
    total_pages = paginator.num_pages
    current_page = page_obj.number
    if total_pages <= 7:
        page_range = paginator.page_range
    else:
        if current_page <= 4:
            page_range = list(range(1, 6)) + ['...'] + [total_pages]
        elif current_page > total_pages - 4:
            page_range = [1] + ['...'] + list(range(total_pages - 4, total_pages + 1))
        else:
            page_range = (
                [1] + ['...']
                + list(range(current_page - 1, current_page + 2))
                + ['...']
                + [total_pages]
            )

    # Cập nhật context
    context = {
        'cate_lv1': cate_lv1,
        'cate_lv2': cate_lv2,
        'page_obj': page_obj,
        'page_range': page_range,
        'breadcrumb': breadcrumb
    }

    return render(request, 'PList_Lv2.html', context)


def TruyenThong(request):
    context = {}
    return render(request,'TruyenThong.html',context)


def TrangChu(request):
    # Lấy 12 sản phẩm bán chạy nhất (sắp xếp theo số lượng bán giảm dần)
    best_sellers = Product.objects.all().order_by('-prod_sold')[:12]
    
    # Lấy sản phẩm và gắn URL của ảnh avatar vào từng sản phẩm
    for product in best_sellers:
        avatar = Product_Image.objects.filter(prod_name=product, is_avatar=True).first()
        product.avatar_url = avatar.ImageURL if avatar else None
    
     # Định dạng giá
        product.prod_price_formatted = "{:,.0f}".format(product.prod_price)

        # Định dạng số đã bán và số lượng đánh giá
        if product.prod_sold > 999:
            product.prod_sold_formatted = "{:.1f}k".format(product.prod_sold / 1000)
        else:
            product.prod_sold_formatted = product.prod_sold

        if product.prod_num_rating > 999:
            product.prod_num_rating_formatted = "{:.1f}k".format(product.prod_num_rating / 1000)
        else:
            product.prod_num_rating_formatted = product.prod_num_rating

        # Định dạng giá giảm
        if product.prod_discount > 0:
            product.prod_discount_formatted = "{:,.0f} đ".format(product.prod_discount)
        else:
            product.prod_discount_formatted = ''

    # Cập nhật số lượng sản phẩm cho tất phân loại 2
    categories_lv2 = Category_lv2.objects.all()
    for category in categories_lv2:
        category.update_num_products()
    # Lấp top 14 phân loại 2 có nhiều sản phẩm nhất
    top_categories = Category_lv2.objects.all().order_by('-num_products')[:14]
        
    context = {
        'page_obj': best_sellers,
        'top_categories': top_categories,
    }
    return render(request, 'TrangChu.html', context)



def ChiTietSanPham(request, cate_lv1_name, cate_lv2_name, product_name):
    # Lấy danh mục cấp 1 và cấp 2 dựa trên tên
    cate_lv1 = get_object_or_404(Category_lv1, cate_1=cate_lv1_name)
    cate_lv2 = get_object_or_404(Category_lv2, cate_2=cate_lv2_name, cate_1=cate_lv1)

    # Lấy sản phẩm
    product = get_object_or_404(Product, prod_name=product_name, prod_cate_lv1=cate_lv1, prod_cate_lv2=cate_lv2)

    # Lấy danh sách ảnh của sản phẩm
    images = Product_Image.objects.filter(prod_name=product)
    images_with_url = [{'url': img.ImageURL, 'is_avatar': img.is_avatar} for img in images]
    
    # Định dạng giá
    product.prod_price_formatted = "{:,.0f}".format(product.prod_price)

    # Định dạng số đã bán và số lượng đánh giá
    if product.prod_sold > 999:
        product.prod_sold_formatted = "{:.1f}k".format(product.prod_sold / 1000)
    else:
        product.prod_sold_formatted = product.prod_sold

    if product.prod_num_rating > 999:
        product.prod_num_rating_formatted = "{:.1f}k".format(product.prod_num_rating / 1000)
    else:
        product.prod_num_rating_formatted = product.prod_num_rating

    # Định dạng giá giảm
    if product.prod_discount > 0:
        product.prod_discount_formatted = "{:,.0f} đ".format(product.prod_discount)
    else:
        product.prod_discount_formatted = ''
    
    # Cập nhật breadcrumb
    breadcrumb = [
        {"name": "Trang chủ", "url": "/"},
        {"name": cate_lv1.cate_1, "url": f"/{cate_lv1.cate_1}/"},
        {"name": cate_lv2.cate_2, "url": f"/{cate_lv1.cate_1}/{cate_lv2.cate_2}/"}
    ]
    
    context = {
        'cate_lv1': cate_lv1,
        'cate_lv2': cate_lv2,
        'product': product,
        'images': images_with_url,
        'breadcrumb': breadcrumb

    }
    return render(request, 'ChiTietSanPham.html', context)
def GioHang(request):  
    cart_items = []
    images_with_url = []

    if request.user.is_authenticated:
        customer = request.user.customer
        # Lấy tất cả các sản phẩm trong giỏ hàng
        cart_items = Cart.objects.filter(cart_customer=customer)

        # Duyệt qua từng sản phẩm để lấy ảnh đại diện và định dạng giá
        for cart_item in cart_items:
            product = cart_item.cart_product

            # Định dạng giá
            product.prod_price_formatted = "{:,.0f}".format(product.prod_price)

            # Lấy ảnh đại diện
            avatar_image = Product_Image.objects.filter(
                prod_name=product, is_avatar=True
            ).first()  # Lấy ảnh avatar đầu tiên nếu có

            if avatar_image:
                images_with_url.append({
                    'product_id': product.id,
                    'url': avatar_image.ImageURL,
                    'is_avatar': avatar_image.is_avatar,
                })

    # Kiểm tra giỏ hàng có rỗng hay không
    if not cart_items:
        empty_cart_message = "Bạn chưa bỏ gì vào giỏ hàng"
    else:
        empty_cart_message = ""

    context = {
        'cart_items': cart_items,
        'images': images_with_url,
        'empty_cart_message': empty_cart_message,  # Thêm thông báo nếu giỏ hàng trống
    }
    return render(request, 'GioHang.html', context)

def TrangCaNhan(request):
    context = { }
    return render(request,'TrangCaNhan.html',context)

def EditTrangCaNhan(request):
    context = { }
    return render(request,'EditTrangCaNhan.html',context)

def DonHangCuaToi(request):
    context = { }
    return render(request,'DonHangCuaToi.html',context)


from django.http import HttpResponse, JsonResponse
import json

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)

    # Lấy sản phẩm trong giỏ hàng hoặc tạo mới nếu chưa có
    cart_item, created = Cart.objects.get_or_create(
        cart_customer=customer,
        cart_product=product
    )

    if action == 'add':
        if created:
            cart_item.cart_product_quantity = 1  # Nếu tạo mới, gán số lượng là 1
        else:
            cart_item.cart_product_quantity += 1  # Nếu đã tồn tại, tăng số lượng
    elif action == 'remove':
        cart_item.cart_product_quantity -= 1
        # Xóa sản phẩm nếu số lượng <= 0
        if cart_item.cart_product_quantity <= 0:
            cart_item.delete()
    elif action == 'remove_all':
        # Xóa sản phẩm bất kể số lượng
        cart_item.delete()

    # Lưu sản phẩm nếu không bị xóa
    if action in ['add', 'remove'] and cart_item.cart_product_quantity > 0:
        cart_item.save()

    return JsonResponse('Sản phẩm đã được cập nhật', safe=False)

# Thêm tự tạo form đăng ký user của django
from django.contrib.auth.forms import UserCreationForm

def DangKy(request):
    form = CreateUserForm()
    if request.method == 'POST':
        # Nếu là post thì gán form bằng cái form bên kia
        form = CreateUserForm(request.POST)
        # kiểm tra xem các trường được điền vào có hợp lệ với điều kiện mặc định của django hay ko
        if form.is_valid():
            form.save()
    context = { 'form': form }
    return render(request,'DangKy.html',context)

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def DangNhap(request):
    # Nếu đã đăng nhập rồi thì về trang chủ
    if request.user.is_authenticated:
        return redirect('TrangChu')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        # Nếu có user này trong dữ liệu thì login
        if user is not None :
            login(request,user)
            return redirect('TrangChu')
        else :
            messages.info(request,'Tên đăng nhập hoặc mật khẩu chưa đúng')
    context = {}
    return render(request,'DangNhap.html',context)

def DangXuat(request):
    logout(request)
    return redirect('DangNhap')