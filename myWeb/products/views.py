from django.shortcuts import render, get_object_or_404
from .models import Category_lv1, Category_lv2
from django.core.paginator import Paginator


from .models import Product, Category_lv1, Category_lv2

from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Product, Category_lv1, Category_lv2, Product_Image
from django.shortcuts import get_object_or_404
from .models import Category_lv1, Category_lv2

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
            product.prod_discount_formatted = "{:,.0f}".format(product.prod_discount)  # xxx.xxx
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
            product.prod_discount_formatted = "{:,.0f}".format(product.prod_discount)
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
            product.prod_discount_formatted = "{:,.0f}".format(product.prod_discount)
        else:
            product.prod_discount_formatted = ''
    
    context = {
        'page_obj': best_sellers,
        
    }
    return render(request, 'TrangChu.html', context)
