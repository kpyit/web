from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.core.files.storage import FileSystemStorage
from django.utils import timezone 


from .forms import ImageForm


import logging

logger = logging.getLogger(__name__)

# def index(request):
#     logger.info('index page accessed')
#     return HttpResponse("HelW")
 
def index(request): 
    logger.debug('index page accessed')
    html_text = """
        <h1>main Vindow</h1>
        <p>la la la </p>
        <p>all good</p>
    """
    return render(request, 'index.html', {'html_text': html_text})

def obout_me(request):
    # Multiline text variable with HTML layout
    logger.debug('obout_me page accessed')
    html_text = """
        <h1>PK</h1>
        <p> </p>
        <p>  </p>
    """
    return render(request, 'obout_me.html', {'html_text': html_text})


def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error in ab page{e}')
        return HttpResponse(" Error ")
    else:
        logger.debug('ab page access')
    return HttpResponse("ab us")



# lab2

from .models import *
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def homepage(request):
    context = {
        'customers': Customer.objects.all(),
        'products': Product.objects.all(),
       'orders': Order.objects.all(),
    }
    return render(request, 'homepage.html', context)

class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    success_url = '/'

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name_suffix = '_update_form'
    success_url = '/'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = '/'

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'quantity']
    success_url = '/'

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'quantity']
    template_name_suffix = '_update_form'
    success_url = '/'

class ProductDelete(DeleteView):
    model = Product
    success_url = '/'

class OrderCreate(CreateView):
    model = Order
    fields = ['good', 'order_total_amount']
    success_url = '/'

class OrderUpdate(UpdateView):
    model = Order
    fields = ['good', 'order_total_amount']
    template_name_suffix = '_update_form'
    success_url = '/'

class OrderDelete(DeleteView):
    model = Order
    success_url = '/'
    




# http://127.O.O.1:8000/product_list/42/week/
def product_list(request,id_user, period):
    now = timezone.now()
    if period == 'week':
        start_date = now - timezone.timedelta(days=7)
    elif period == 'month':
        start_date = now - timezone.timedelta(days=30)
    elif period == 'year':
        start_date = now - timezone.timedelta(days=365)
    else:
        raise ValueError('Invalid period')
    
    try:
        cur_customer = Customer.objects.get(pk=id_user)
        # context = {'customer': customer}        
    except Customer.DoesNotExist:
        raise Http404("Customer does not exist")

    # customer_orders = Order.objects.filter(customer=request.user, order_date__gte=start_date)
    customer_orders = Order.objects.filter(customer=cur_customer, order_date__gte=start_date)
    products = Product.objects.filter(order__in=customer_orders).distinct()

    return render(request, 'product_list.html', {'cur_customer': cur_customer,'products': products,'customer_orders':customer_orders})

# pk - первичный ключ
# http://127.0.0.1:8000/product/4/form_image/
def product_add_image(request, pk_prod):
    # загрузка продукта
    try:
        cur_product = Product.objects.get(pk=pk_prod)
        # context = {'cur_product': cur_product}        
    except Customer.DoesNotExist:
        raise Http404("Customer does not exist")
    logger.info('user getted')
    
    if request.method == 'POST':
        logger.info('image POST')
        # form = ImageForm(request.POST, request.FILES)
        form = ImageForm(request.POST,request.FILES)
        logger.info('request.FILES')
        if form.is_valid():
            logger.info('image'+form.cleaned_data['image_l'].name)
        # image = form['image']
            image_ll = form.cleaned_data['image_l']
            logger.info('igm  '+image_ll.name)
            
            fs = FileSystemStorage()# работа с файловой системой
            fs.save(image_ll.name, image_ll)
            
            cur_product.photo = image_ll.name
            cur_product.save()
        else:
            logger.info('not valid')
            
        # form = ImageForm()
        return render(request, 'image_form_product.html', {'form':form,'cur_product': cur_product})


    else: 
        form = ImageForm()
        return render(request, 'image_form_product.html', {'form':form,'cur_product': cur_product})
            
        





    



