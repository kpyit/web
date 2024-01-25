from django.urls import path 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('obout_me', views.obout_me, name='obout_me'),
    path('about', views.about, name='about'),    
]
