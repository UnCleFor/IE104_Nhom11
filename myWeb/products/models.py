from django import forms
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Tạo class để thay đổi form đăng nhập của django bằng cách kế thừa class UserCreationForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nhập tên đăng nhập'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nhập email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nhập tên'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nhập họ'
            }),
            # 2 cái dưới này lỗi ko load được
            'password1': forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nhập mật khẩu'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nhập lại mật khẩu'
            }),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already taken.')
        return email
    
    # def clean_password2(self):
    #     # Lấy dữ liệu từ cả hai trường mật khẩu
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Mật khẩu không khớp. Vui lòng kiểm tra lại.")
    #     return password2



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
    def update_num_products(self):
       
        # Cập nhật số lượng sản phẩm trong danh mục cấp 2.
        
        self.num_products = Product.objects.filter(prod_cate_lv2=self).count()
        self.save()

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

    prod_description = models.CharField(max_length=500,null=True, blank=False)
    prod_ingredient = models.CharField(max_length=500,null=True, blank=False)
    prod_who_to_use = models.CharField(max_length=500,null=True, blank=False)
    prod_how_to_use = models.CharField(max_length=500,null=True, blank=False)
    prod_brand = models.CharField(max_length=500,null=True, blank=False)
    prod_country = models.CharField(max_length=500,null=True, blank=False)
    prod_effect = models.CharField(max_length=500,null=True, blank=False)
    prod_side_effect = models.CharField(max_length=500,null=True, blank=False)
    prod_preserve= models.CharField(max_length=500,null=True, blank=False)

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

class Cart(models.Model):
    cart_customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    cart_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    cart_product_quantity = models.IntegerField(default=1)
    is_selected = models.BooleanField(default=False)  # Trạng thái chọn/deselect sản phẩm
    
    def __str__(self) -> str:
        return f"Giỏ hàng của {self.cart_customer.username}: {self.cart_product.prod_name}"
    class Meta:
        unique_together = ('cart_customer', 'cart_product')  # Một khách hàng không thể thêm trùng sản phẩm vào giỏ

    @property
    def get_total_cart(self):
        # Tính tổng tiền cho sản phẩm này nếu được chọn
        if self.is_selected:
            return self.cart_product.prod_price * self.cart_product_quantity
        return 0

    @staticmethod
    def calculate_selected_total(user):
        # Lấy tất cả các mục trong giỏ hàng của người dùng và đã được chọn
        selected_items = Cart.objects.filter(cart_customer=user, is_selected=True)
        # Tính tổng tiền từ tất cả các mục
        total = sum(item.cart_product.prod_price * item.cart_product_quantity for item in selected_items)
        return total
        
class Order(models.Model):
    UNIT_TYPE_CHOICES = [
        
        ('Đang xử lý', 'Đang xử lý'),
        ('Đang giao', 'Đang giao'),
        ('Đã giao', 'Đã giao'),
        ('Đã hủy', 'Đã hủy'),
        ('Trả hàng', 'Trả hàng'),
    ]
    METHOD_CHOICE = [
        ('Thanh toán tiền mặt khi nhận hàng', 'Thanh toán tiền mặt khi nhận hàng'),
        ('Thanh toán bằng thẻ ATM nội địa và tài khoản ngân hàng', 'Thanh toán bằng thẻ ATM nội địa và tài khoản ngân hàng'),
    ]
    order_customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    order_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=100,choices=UNIT_TYPE_CHOICES)
    order_total = models.IntegerField(null=True,blank=False)
    order_method = models.CharField(max_length=100,choices=METHOD_CHOICE)
    
    order_receiver_name = models.CharField(max_length=100,null=True,blank=False)
    order_receiver_phone = models.CharField(max_length=15,null=True,blank=False)
    order_adress = models.CharField(max_length=100,null=True,blank=False)

    def __str__(self) -> str:
        return f"Đơn hàng từ {self.order_customer} vào ngày {self.order_date}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    quantity = models.IntegerField(null=True,blank=False)
    
    def __str__(self) -> str:
        return f"Đơn {self.order.order_customer} vào ngày {self.order.order_date} mua {self.product.prod_name}"
