from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age {self.age}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    decription = models.TextField()
    image = models.ImageField(upload_to='products/')
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)#автоустановка
    total_price = models.DecimalField(max_digits=8, decimal_places=2)# стандарнтная запись
    
    
    