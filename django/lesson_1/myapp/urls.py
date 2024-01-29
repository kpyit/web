from django.urls import path 
# from . import views
from .views import *
app_name = 'myapp'
urlpatterns = [ 
    # path('', index, name='index'),
    path('obout_me', obout_me, name='obout_me'),
    path('about', about, name='about'),  
    
    # lab2
    path('', homepage),
    path('create_customer/', CustomerCreate.as_view(), name="create_customer"),
    path('<int:pk>/update_customer/', CustomerUpdate.as_view()),
    path('<int:pk>/delete_customer/', CustomerDelete.as_view()),
    path('create_product/', ProductCreate.as_view(), name="create_product"),
    path('<int:pk>/update_product/', ProductUpdate.as_view()),
    path('<int:pk>/delete_product/', ProductDelete.as_view()),
    path('create_order/', OrderCreate.as_view(), name="create_order"),
    path('<int:pk>/update_order/', OrderUpdate.as_view()),
    path('<int:pk>/delete_order/', OrderDelete.as_view()),  
] 