from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


from django.core.paginator import Paginator
from django.shortcuts import render

from django.core.paginator import Paginator
from django.shortcuts import render

def PList_ThucPhamChucNang(request):
    # Dummy data: 100 sản phẩm mẫu
    products = [
        {"name": f"Product {i}", 
         "img": "img/product/paracetalmol.jpg", 
         "old_price": "120.000 đ", 
         "new_price": f"{100 + i}.000 đ", 
         "likes": f"{35 + i}.1k", 
         "sold": f"{6 + i}.5k"}
        for i in range(1, 98)  # Tạo 100 sản phẩm
    ]
    
    # Phân trang với 12 sản phẩm mỗi trang
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Xử lý hiển thị phân trang rút gọn
    total_pages = paginator.num_pages
    current_page = page_obj.number
    page_range = []

    # Hiển thị 3 trang đầu, 3 trang cuối, và 3 trang gần trang hiện tại
    if total_pages <= 7:
        page_range = paginator.page_range
    else:
        if current_page <= 4:
            page_range = list(range(1, 6)) + ['...'] + [total_pages]
        elif current_page > total_pages - 4:
            page_range = [1] + ['...'] + list(range(total_pages - 4, total_pages + 1))
        else:
            page_range = [1] + ['...'] + list(range(current_page - 1, current_page + 2)) + ['...'] + [total_pages]

    context = {
        'page_obj': page_obj,
        'page_range': page_range,
    }
    return render(request, 'PList_ThucPhamChucNang.html', context)

