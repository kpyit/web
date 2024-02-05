from django.db import models

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()
    
#     def __str__(self):
#         return f'Username: {self.name}, email: {self.email}, age {self.age}'
    
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     decription = models.TextField()
#     image = models.ImageField(upload_to='products/')
    
# class Order(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     date_ordered = models.DateTimeField(auto_now_add=True)#автоустановка
#     total_price = models.DecimalField(max_digits=8, decimal_places=2)# стандарнтная запись

class Customer(models.Model):
    # Поля модели клиента
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)#'client registration date'

    def __str__(self):
        return self.name

class Product(models.Model): 
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    photo = models.CharField(max_length=255, default = "")
    # photo = models.ImageField(upload_to="product_photos/") # Adding Image Field

    def __str__(self):
        return self.name

class Order(models.Model):
    # Связывание полей между моделями заказа и клиента
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Связующее поле между моделью заказа и моделью товара
    good = models.ManyToManyField(Product)

    # Другие поля модели заказа
    order_total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # order_date = models.DateTimeField(auto_now_add=True)#'order placement date'
    order_date = models.DateTimeField()#'order placement date'

    def __str__(self):
        return f'{self.customer} - {self.id}'
     