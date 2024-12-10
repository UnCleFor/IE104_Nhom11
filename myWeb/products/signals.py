from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product, Category_lv2

@receiver(post_save, sender=Product)
def update_category_product_count_on_product_save(sender, instance, **kwargs):
    # Lấy danh mục cấp 2 từ sản phẩm
    category_lv2 = instance.prod_cate_lv2
    if category_lv2:
        # Cập nhật số lượng sản phẩm trong danh mục, nếu chưa có thì bắt đầu từ 0
        category_lv2.num_products = Product.objects.filter(prod_cate_lv2=category_lv2).count() if category_lv2 else 0
        category_lv2.save()

@receiver(post_delete, sender=Product)
def update_category_product_count_on_product_delete(sender, instance, **kwargs):
    # Lấy danh mục cấp 2 từ sản phẩm
    category_lv2 = instance.prod_cate_lv2
    if category_lv2:
        # Cập nhật số lượng sản phẩm trong danh mục, nếu chưa có thì bắt đầu từ 0
        category_lv2.num_products = Product.objects.filter(prod_cate_lv2=category_lv2).count() if category_lv2 else 0
        category_lv2.save()
