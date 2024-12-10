from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null=True, blank= False)
    user_name = models.CharField(max_length=500)
    user_birth = models.DateField()
    user_phone = models.CharField(max_length=15)
    user_email = models.EmailField(max_length=100, null =True)

    def __str__(self) -> str:
        return self.user_name

class Category_lv1(models.Model):
    cate_1 = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.cate_1

class Category_lv2(models.Model):
    cate_1 = models.ForeignKey(Category_lv1, on_delete=models.SET_NULL, null=True, blank=False)
    cate_2 = models.CharField(max_length=500)
    cate_2_image = models.ImageField(null=True, blank=False)
    num_products = models.IntegerField(default=0)  # Field to store the count of products

    def __str__(self) -> str:
        return self.cate_2


class Product(models.Model):
    UNIT_TYPE_CHOICES = [
        ('Hộp', 'Hộp'),
        ('Tuýt', 'Tuýt'),
        ('Ống', 'Ống'),
        ('Viên', 'Viên'),
    ]

    prod_name = models.CharField(max_length=500)
    prod_price = models.IntegerField()
    prod_discount = models.IntegerField()
    prod_cate_lv1 = models.ForeignKey(Category_lv1, on_delete=models.SET_NULL, null=True, blank=False)
    prod_cate_lv2 = models.ForeignKey(Category_lv2, on_delete=models.SET_NULL, null=True, blank=False)
    prod_num_available = models.IntegerField()
    prod_sold = models.IntegerField()
    prod_num_rating = models.IntegerField()
    prod_unit_type = models.CharField(max_length=50, choices=UNIT_TYPE_CHOICES,null=True,blank=False)

    def __str__(self) -> str:
        return self.prod_name

class Product_Image(models.Model):
    prod_name = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    prod_image = models.ImageField(null=True, blank=False)
    is_avatar = models.BooleanField(default=False)

    def __str__(self):
        # Kiểm tra nếu có liên kết tới sản phẩm
        if self.prod_name:
            if self.is_avatar:
                return f"avatar_{self.prod_name.prod_name}"  # avatar + tên sản phẩm
            return self.prod_name.prod_name  # Chỉ tên sản phẩm
        return "Unknown Product Image"  # Dự phòng nếu không có sản phẩm
    
    @property
    def ImageURL(self):
        try:
            url = self.prod_image.url
        except :
            url = ''
        return url