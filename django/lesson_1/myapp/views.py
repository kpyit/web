from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

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