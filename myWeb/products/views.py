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
    if request.user.is_authenticated:
        customer = request.user
        cart_items = Cart.objects.filter(cart_customer=customer)

       

        images_with_url = []
        for cart_item in cart_items:
            product = cart_item.cart_product
            product.prod_price_formatted = "{:,.0f}".format(product.prod_price)
            avatar_image = Product_Image.objects.filter(prod_name=product, is_avatar=True).first()

            if avatar_image:
                images_with_url.append({
                    'product_id': product.id,
                    'url': avatar_image.ImageURL,
                    'is_avatar': avatar_image.is_avatar,
                })
        
        total_selected_price = "{:,.0f} đ".format(Cart.calculate_selected_total(customer))   # Tính tổng tiền các sản phẩm được chọn

        empty_cart_message = "Bạn chưa bỏ gì vào giỏ hàng" if not cart_items else ""
        context = {
            'cart_items': cart_items,
            'images': images_with_url,
            'empty_cart_message': empty_cart_message,
            'total_selected_price': total_selected_price,
        }
        return render(request, 'GioHang.html', context)






from django.http import HttpResponse, JsonResponse
import json

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id=productId)

    # Lấy sản phẩm trong giỏ hàng hoặc tạo mới nếu chưa có
    cart_item, created = Cart.objects.get_or_create(
        cart_customer=customer,
        cart_product=product
    )

    if action == 'select':
        cart_item.is_selected = not cart_item.is_selected  # Đảo trạng thái của is_selected
    elif action == 'add':
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
    if action in ['add', 'remove','select'] and cart_item.cart_product_quantity > 0:
        cart_item.save()

    return JsonResponse('Sản phẩm đã được cập nhật', safe=False)


# Thêm tự tạo form đăng ký user của django
from django.contrib.auth.forms import UserCreationForm

def DangKy(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Đăng ký thành công!'})
        else:
            # Trả về các lỗi dạng JSON
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'DangKy.html', context)

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def DangNhap(request):
    # Nếu đã được đăng nhập rồi thì trở lại trang chủ
    if request.user.is_authenticated:
        return redirect('TrangChu')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Đăng nhập thành công!', 'redirect_url': 'TrangChu'})
        else:
            return JsonResponse({'success': False, 'message': 'Tên đăng nhập hoặc mật khẩu chưa đúng'})

    return render(request, 'DangNhap.html')

def DangXuat(request):
    logout(request)
    return redirect('DangNhap')

from django.shortcuts import render, redirect
from .models import Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from .models import Cart, Product_Image, Order, OrderItem
from django.contrib import messages

def DatHang(request):
    customer = request.user  # Lấy thông tin người dùng đang đăng nhập
    if not customer.is_authenticated:
        return redirect('login')  # Chuyển hướng nếu người dùng chưa đăng nhập

    selected_cart_items = Cart.objects.filter(cart_customer=customer, is_selected=True)

    # Tạo context cho các sản phẩm được chọn và hình ảnh đại diện của sản phẩm
    images_with_url = []
    total_price = 0  # Tổng tiền phải trả

    for cart_item in selected_cart_items:
        product = cart_item.cart_product
        quantity = cart_item.cart_product_quantity
        price = product.prod_price

        item_total_price = price * quantity
        cart_item.item_total_price = "{:,.0f}".format(item_total_price)
        total_price += item_total_price

        # Định dạng giá sản phẩm
        product.prod_price_formatted = "{:,.0f}".format(price)

        avatar_image = Product_Image.objects.filter(prod_name=product, is_avatar=True).first()
        if avatar_image:
            images_with_url.append({
                'product_id': product.id,
                'url': avatar_image.ImageURL,
                'is_avatar': avatar_image.is_avatar,
            })

    total_price_formatted = "{:,.0f}".format(total_price)

    context = {
        'cart_items': selected_cart_items,
        'images': images_with_url,
        'total_price': total_price_formatted,
    }

    if request.method == 'POST':
        # Lấy thông tin nhận hàng từ POST request
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        if full_name and phone_number and address and payment_method:
            # Tạo đơn hàng mới
            order = Order(
                order_customer=customer,
                order_status='Đang xử lý',
                order_total=total_price,
                order_method=payment_method,
                
                order_receiver_name = full_name,
                order_receiver_phone = phone_number,
                order_adress = address,
            )
            order.save()

            # Thêm các sản phẩm vào đơn hàng
            for cart_item in selected_cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.cart_product,
                    quantity=cart_item.cart_product_quantity
                )

            # Xóa các sản phẩm đã được thêm vào đơn hàng khỏi giỏ hàng
            selected_cart_items.delete()

            # Hiển thị thông báo thành công
            messages.success(request, "Đặt hàng thành công!")
            return redirect('DonHangCuaToi')

        else:
            messages.error(request, "Vui lòng điền đầy đủ thông tin nhận hàng và chọn phương thức thanh toán.")

    return render(request, 'DatHang.html', context)

def DonHangCuaToi(request):
    customer = request.user
    order_list = Order.objects.filter(order_customer=customer)
    order_details = []

    # Lấy chi tiết từng đơn hàng
    for order in order_list:
        order_items = OrderItem.objects.filter(order=order)
        items_info = []
        for item in order_items:
            avatar_image = Product_Image.objects.filter(prod_name=item.product, is_avatar=True).first()
            image_url = avatar_image.ImageURL if avatar_image else ''  # URL của ảnh đại diện
            items_info.append({
                'product_name': item.product.prod_name,
                'quantity': item.quantity,
                'price': item.product.prod_price,
                'product_unit_type': item.product.prod_unit_type,
                'total_price': "{:,.0f}".format(item.quantity * item.product.prod_price),  # Tính tổng tiền
                'image_url': image_url,  # URL hình ảnh sản phẩm
            })
        order_details.append({
            'order_id': order.id,
            'order_date': order.order_date,
            'order_status': order.order_status,
            'order_total': "{:,.0f}".format(order.order_total),
            'order_method': order.order_method,
            'receiver_name': order.order_receiver_name,
            'receiver_phone': order.order_receiver_phone,
            'receiver_address': order.order_adress,
            'items': items_info,
        })

    context = {
        'order_details': order_details,
    }

    return render(request, 'DonHangCuaToi.html', context)

def ChiTietDonHang(request,order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {}
    return render(request, 'ChiTietDonHang.html',context)

def TrangCaNhan(request):
    customer = request.user
    context = { 
        'customer': customer
        }
    return render(request,'TrangCaNhan.html',context)



from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

@login_required
def EditTrangCaNhan(request):
    if request.method == 'POST':
        user = request.user
        new_username = request.POST.get('username')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_email = request.POST.get('email')

        # Kiểm tra các trường không được để trống
        if not new_username or not new_first_name or not new_last_name or not new_email:
            messages.error(request, "Vui lòng không bỏ trống bất kỳ trường nào!")
            return render(request, 'EditTrangCaNhan.html')

        # Kiểm tra địa chỉ email hợp lệ
        try:
            validate_email(new_email)
        except ValidationError:
            messages.error(request, "Địa chỉ email không hợp lệ!")
            return render(request, 'EditTrangCaNhan.html')

        # Kiểm tra xem username đã tồn tại chưa
        if User.objects.filter(username=new_username).exclude(id=user.id).exists():
            messages.error(request, "Tên người dùng đã được sử dụng!")
            return render(request, 'EditTrangCaNhan.html')

        # Kiểm tra xem email đã tồn tại chưa
        if User.objects.filter(email=new_email).exclude(id=user.id).exists():
            messages.error(request, "Email đã được sử dụng bởi tài khoản khác!")
            return render(request, 'EditTrangCaNhan.html')

        # Lưu thông tin mới vào cơ sở dữ liệu
        user.username = new_username
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.email = new_email
        user.save()
        return redirect('TrangCaNhan')

    return render(request, 'EditTrangCaNhan.html')
def TimKiem(request):
    if request.method == "POST":
        searched = request.POST.get("searched", "").strip()
        if not searched:
            return redirect('TrangChu')  # Redirect về trang chủ nếu không có gì được tìm kiếm

        keys = Product.objects.filter(prod_name__icontains=searched)

        if not keys.exists():
            no_results_message = "Không có kết quả trùng khớp cho tìm kiếm của bạn."
            context = {
                'no_results_message': no_results_message if not keys.exists() else None,
                'searched': searched,
            }
            return render(request, 'TimKiem.html', context)
        else:
            # Lấy sản phẩm và gắn URL của ảnh avatar vào từng sản phẩm
            for product in keys:
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

            # Phân trang với 12 sản phẩm mỗi trang
            paginator = Paginator(keys, 12)
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

        context = {
            'page_obj': page_obj,
            'page_range': page_range,
            'searched': searched,
            'no_results_message': no_results_message if not keys.exists() else None,
        }
        return render(request, 'TimKiem.html', context)

