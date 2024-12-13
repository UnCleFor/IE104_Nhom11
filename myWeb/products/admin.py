from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category_lv1)
admin.site.register(Category_lv2)
admin.site.register(Product)
admin.site.register(Product_Image)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)
admin.site.register(Cart)