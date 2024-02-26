from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('dashboard.html/', views.dashboard),
    path('products/', views.products, name='products')  ,
    path('customer/<str:pk>', views.customer, name='customer'),
]