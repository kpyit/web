# com_gen_data.py

from django.core.management.base import BaseCommand 
from myapp.models import * 

from faker import Faker
import random

from django.utils import timezone 
import datetime


fakegen = Faker()

class Command(BaseCommand):
    help = "Add user and prod"

    # оставил чтобы не забыть опцию
    def add_argumetns(self, parser):
        # parser.add_argument('age', type=int, help='User ID')
        # parser.add_argument('name', type=str, help='User name')
        None

    def handle(self, *args, **kwargs):
        # pk = kwargs.get('pk')
        # name = kwargs.get('name')
            
        generate_customers()
        generate_products()
        generate_orders() 
             
        self.stdout.write(f'all created')# тут вызов __str__
 
         
def generate_customers():
    customers = []
    for _ in range(10):
        cus = Customer(name = fakegen.name(), email = fakegen.email(), phone_number = int(''.join([str(random.randint(0,9)) for i in range(10)])), address = fakegen.address())
        customers.append(cus)
    #  Save в базу
    Customer.objects.bulk_create(customers)
    
def generate_products():
    products = []
    for _ in range(20):
        prod = Product(name = ' '.join(fakegen.words(3)), description = fakegen.text(), price = round(random.uniform(50.99, 499.99), 2), quantity = random.randint(1,30))
        products.append(prod)
    Product.objects.bulk_create(products)
        
def generate_orders():
    orders = []
    all_customers = list(Customer.objects.all())
    all_products = list(Product.objects.all())
    for _ in range(50):
        cust = random.choice(all_customers)
        num_of_prods = random.randint(1, len(all_products))
        selected_products = random.sample(all_products, num_of_prods)
        total_price = 0
        for product in selected_products:
            total_price += product.price
            
        # ругается на таймзону но тут это не важно
        fake_order_date = fakegen.date_time_between(start_date='-1y', end_date='now')
        ordr = Order(customer = cust, order_total_amount = total_price, order_date=fake_order_date)        
        # ordr = Order(customer = cust, order_total_amount = total_price)
        ordr.save()   # перед добавлением полей m2m необходимо сначала сохранить
        ordr.good.set(selected_products) # добавляем отношения "многие-ко-многим"
        orders.append(ordr)
         