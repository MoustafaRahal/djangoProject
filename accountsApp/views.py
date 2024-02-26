from django.shortcuts import render
from django.http import HttpResponse

from accountsApp.models import *


# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending_orders = orders.filter(status='pending').count()
    delivered_orders = orders.filter(status='delivered').count()
    context = {'orders': orders, 'customers': customers
               , 'total_customers': total_customers, 'total_orders': total_orders
               , 'pending_orders': pending_orders, 'delivered_orders': delivered_orders}
    return render(request, '../templates/dashboard.html', context)

#def dashboard(request):
#    return render(request, 'accountsApp/dashboard.html')


def products(request):
    products = Product.objects.all()
    return render(request, '../templates/products.html', {'products': products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    context = {'customer': customer, 'orders': orders}
    return render(request, '../templates/customer.html', context)